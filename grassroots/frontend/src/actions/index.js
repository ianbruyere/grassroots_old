export const REQUEST_CONGRESS_MEMBERS = 'REQUEST_CONGRESS_MEMBERS'
export const RECIEVE_CONGRESS_MEMBERS = 'RECIEVE_CONGRESS_MEMBERS'
export const SELECT_CONGRESS_MEMBER = 'SELECT_CONGRESS_MEMBER'
export const SELECT_STATE = 'SELECT_STATE'
export const RECIEVE_SELECT_CONGRESS_MEMBER = 'RECIEVE_SELECT_CONGRESS_MEMBER'
export const REQUEST_BILL = 'REQUEST_BILL'
export const RECIEVE_BILL = 'RECIEVE_BILL'

export function requestBill(url) {
    return {
        type: REQUEST_BILL,
        url
    }
}

export function recieveBill(json) {
    return {
        type: RECIEVE_BILL,
        bill: json
    }
}

export function selectState(state) {
    return {
        type: SELECT_STATE,
        state
    }
}
export function requestCongressMembers(state) {
    return {
        type: REQUEST_CONGRESS_MEMBERS,
        state
    }
}

export function recieveCongressMembers(state, json) {
    return {
        type: RECIEVE_CONGRESS_MEMBERS,
        state,
        congressMembers: json 
    }
}

export function recieveSelectCongressMember(json) {
    return {
        type: RECIEVE_SELECT_CONGRESS_MEMBER,
        congressMembers: json
    }
}

export function selectCongressMember(memberId) {
    return {
        type: SELECT_CONGRESS_MEMBER,
        memberId
    }
}
