from typing import Tuple, List

from algosdk.v2client.algod import AlgodClient
from algosdk.future import transaction
from algosdk.logic import get_application_address
from algosdk import account, encoding

from pyteal import compileTeal, Mode

from account import Account
from contracts import approval_program, clear_state_program
from util import (
    waitForTransaction,
    fullyCompileContract,
    getAppGlobalState,
)

APPROVAL_PROGRAM = b""
CLEAR_STATE_PROGRAM = b""


def getContracts(client: AlgodClient) -> Tuple[bytes, bytes]:
    """Get the compiled TEAL contracts.

    Args:
        client: An algod client that has the ability to compile TEAL programs.

    Returns:
        A tuple of 2 byte strings. The first is the approval program, and the
        second is the clear state program.
    """
    global APPROVAL_PROGRAM
    global CLEAR_STATE_PROGRAM

    if len(APPROVAL_PROGRAM) == 0:
        APPROVAL_PROGRAM = fullyCompileContract(client, approval_program())
        CLEAR_STATE_PROGRAM = fullyCompileContract(client, clear_state_program())

    return APPROVAL_PROGRAM, CLEAR_STATE_PROGRAM


def createCrowdfundingPool(
    client: AlgodClient,
    sender: Account,
    projectName: str,
    projectDesc: str,
    goalAmount: int
) -> int:
    """Create a new crowdfunding pool.

    Args:
        client: An algod client.
        sender: The account that will create the crowdfunding pool.
        projectName: The name of the crowdfunding project.
        projectDesc: The description of the crowdfunding project.
        endTime: A UNIX timestamp representing the end time of the funding process. This
            must be greater than the current timestamp.
        goalAmount: The funding goal for the crowdfunding project. If the time ends before
        the goal is reached, all funds are returned to backers.

    Returns:
        The ID of the newly created crowdfunding pool.
    """

    approval, clear = getContracts(client)
    globalSchema = transaction.StateSchema(num_uints=10, num_byte_slices=10)
    localSchema = transaction.StateSchema(num_uints=0, num_byte_slices=0)

    app_args = [
        sender.getAddress(),
        projectName,
        projectDesc,
        endTime.to_bytes(8, "big"),
        goalAmount.to_bytes(8, "big"),
    ]

    txn = transaction.ApplicationCreateTxn(
        sender=sender.getAddress(),
        on_complete=transaction.OnComplete.NoOpOC,
        approval_program=approval,
        clear_program=clear,
        global_schema=globalSchema,
        local_schema=localSchema,
        app_args=app_args,
        sp=client.suggested_params(),
    )

    signedTxn = txn.sign(sender.getPrivateKey())

    client.send_transaction(signedTxn)

    response = waitForTransaction(client, signedTxn.get_txid())
    assert response.applicationIndex is not None and response.applicationIndex > 0
    
    return response.applicationIndex


def fundProject(
    client: AlgodClient, 
    appID: int, 
    backer: Account, 
    amount: int
):
    """Place a bid on an active auction.

    Args:
        client: An Algod client.
        appID: The app ID of the auction.
        bidbackerder: The account providing the funds.
        amount: The amount of funds to back the project with.
    """

    appAddr = get_application_address(appID)
    appGlobalState = getAppGlobalState(client, appID)
    suggestedParams = client.suggested_params()

    payTxn = transaction.PaymentTxn(
        sender=backer.getAddress(),
        receiver=appAddr,
        amt=amount,
        sp=suggestedParams,
    )

    appCallTxn = transaction.ApplicationCallTxn(
        sender=bidder.getAddress(),
        index=appID,
        on_complete=transaction.OnComplete.NoOpOC,
        app_args=[b"fund"],
        sp=suggestedParams,
    )

    transaction.assign_group_id([payTxn, appCallTxn])

    signedPayTxn = payTxn.sign(bidder.getPrivateKey())
    signedAppCallTxn = appCallTxn.sign(bidder.getPrivateKey())

    client.send_transactions([signedPayTxn, signedAppCallTxn])

    waitForTransaction(client, appCallTxn.get_txid())


def closeCrowdfundingPool(
    client: AlgodClient, 
    appID: int, 
    closer: Account
):
    """Close a crowdfunding pool.

    This action can only happen after the funding process ends. If successful,
    the creator can withdraw all funds. If not, they are returned to the backers.

    Args:
        client: An Algod client.
        appID: The app ID of the auction.
        closer: The account initiating the close transaction. 
            This can be any account.
    """

    appGlobalState = getAppGlobalState(client, appID)
    accounts: List[str] = [encoding.encode_address(appGlobalState[b"creator"])]

    deleteTxn = transaction.ApplicationDeleteTxn(
        sender=closer.getAddress(),
        index=appID,
        accounts=accounts,
        sp=client.suggested_params(),
    )
    signedDeleteTxn = deleteTxn.sign(closer.getPrivateKey())

    client.send_transaction(signedDeleteTxn)

    waitForTransaction(client, signedDeleteTxn.get_txid())
