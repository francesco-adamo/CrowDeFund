export function setAuthenticated(state, value) {
    state.authenticated = value;
}

export function setAdministrator(state, value) {
    state.administrator = value;
}

export function setViewing(state, value) {
    state.viewing = value;
}

export function setUsername(state, username) {
    state.username = username;
}

export function setPassword(state, password) {
    state.password = password;
}

export function setUserData(state, userData) {
    state.userData = userData;
}

export function updateUserData(state, { property, value }) {
    state.userData[property] = value; 
}

export function setUsersList(state, usersList) {
    state.usersList = usersList;
}

export function updateUsersList(state, { user, updateObject }) {
    if (!state.usersList[user]) state.usersList[user] = {};
    for (const property in updateObject) {
        state.usersList[user][property] = updateObject[property];
    }  
}

export function removeFromUsersList(state, user) {
    delete state.usersList[user];
}

export function setSaved(state, saved) {
    state.saved = saved;
}

export function reset(state) {
    state.authenticated = false;
    state.administrator = false;
    state.viewing = false;
    state.username = '';
    state.password = '';
    state.userData = {};
    state.usersList = {};
    state.saved = {};
}
