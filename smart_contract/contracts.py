from pyteal import *

def approval_program():
    creator = Bytes("creator")
    project_name = Bytes("project_name")
    project_desc = Bytes("project_desc")
    start_time = Bytes("start_time")
    end_time = Bytes("end_time")
    goal_amount = Bytes("goal_amount")
    backers = Bytes("backers")

    # CREATE PROJECT POOL

    on_create_end_time = Btoi(Txn.application_args[3])
    on_create = Seq(
        Assert(Global.latest_timestamp() < on_create_end_time),

        App.globalPut(creator, Txn.application_args[0]),
        App.globalPut(project_name, Txn.application_args[1]),
        App.globalPut(project_desc, Txn.application_args[2]),
        App.globalPut(start_time, Global.latest_timestamp()),
        App.globalPut(end_time, on_create_end_time),
        App.globalPut(goal_amount, Btoi(Txn.application_args[4])),
        App.globalPut(backers, Int(0)),

        # initial funding of 0.5 ALGOs
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields(
            {
                TxnField.type_enum: TxnType.Payment,
                TxnField.amount: Int(500000),
                TxnField.receiver: Global.current_application_address(),
            }
        ),
        InnerTxnBuilder.Submit(),

        Approve(),
    )

    # FUND PROJECT

    on_fund_txn_index = Txn.group_index() - Int(1)
    on_fund_current_backers = App.globalGet(backers)
    on_fund = Seq(
        Assert(
            And(
                # the project has not ended
                Global.latest_timestamp() < App.globalGet(end_time),
                # the actual fund payment is before the app call
                Gtxn[on_fund_txn_index].type_enum() == TxnType.Payment,
                Gtxn[on_fund_txn_index].sender() == Txn.sender(),
                Gtxn[on_fund_txn_index].receiver() == Global.current_application_address(),
                Gtxn[on_fund_txn_index].amount() >= Global.min_txn_fee(),
            )
        ),

        # save backer amount with key: backer_index + a
        App.globalPut(Concat(on_fund_current_backers, Bytes("a")), Gtxn[on_fund_txn_index].amount()),
        # save backer pubkey with key: backer_index + k
        App.globalPut(Concat(on_fund_current_backers, Bytes("k")), Gtxn[on_fund_txn_index].sender()),
        # increase counter
        App.globalPut(backers, on_fund_current_backers + Int(1)),

        Approve(),
    )

    # CLOSE PROJECT POOL

    i = ScratchVar(TealType.uint64)
    length = ScratchVar(TealType.uint64)
    on_delete = Seq(
        Assert(App.globalGet(end_time) <= Global.latest_timestamp()),

        If(Balance(Global.current_application_address()) < App.globalGet(goal_amount))
        .Then(
            # the goal was not reached -- return funds to backers
            Seq(
                length.store(App.globalGet(backers)),
                For(i.store(Int(0)), i.load() < length.load(), i.store(i.load() + Int(1)))
                .Do(
                    Seq(
                        InnerTxnBuilder.Begin(),
                        InnerTxnBuilder.SetFields(
                            {
                                TxnField.type_enum: TxnType.Payment,
                                TxnField.amount: App.globalGet(Concat(Itob(i.load()), Bytes("a"))) - Global.min_txn_fee(),
                                TxnField.receiver: App.globalGet(Concat(Itob(i.load()), Bytes("k"))),
                            }
                        ),
                        InnerTxnBuilder.Submit(),
                    )
                )
            )
        ),
            
        # send all remaining funds to creator
        InnerTxnBuilder.Begin(),
        InnerTxnBuilder.SetFields(
            {
                TxnField.type_enum: TxnType.Payment,
                TxnField.close_remainder_to: App.globalGet(creator),
            }
        ),
        InnerTxnBuilder.Submit(),

        Approve(),
    )

    # ROUTING

    on_call_method = Txn.application_args[0]
    on_call = Cond(
        [on_call_method == Bytes("fund"), on_fund],
    )

    program = Cond(
        [Txn.application_id() == Int(0), on_create],
        [Txn.on_completion() == OnComplete.NoOp, on_call],
        [Txn.on_completion() == OnComplete.DeleteApplication, on_delete],
        [
            Or(
                Txn.on_completion() == OnComplete.OptIn,
                Txn.on_completion() == OnComplete.CloseOut,
                Txn.on_completion() == OnComplete.UpdateApplication,
            ),
            Reject(),
        ],
    )
    return program


def clear_state_program():
    return Approve()


if __name__ == "__main__":
    with open("crowdfunding_approval.teal", "w") as f:
        compiled = compileTeal(approval_program(), mode=Mode.Application, version=5)
        f.write(compiled)

    with open("crowdfunding_clear_state.teal", "w") as f:
        compiled = compileTeal(clear_state_program(), mode=Mode.Application, version=5)
        f.write(compiled)
