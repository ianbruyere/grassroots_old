export const REQUEST_CONGRESS_MEMBERS = 'REQUEST_CONGRESS_MEMBERS'
export const RECIEVE_CONGRESS_MEMBERS = 'RECIEVE_CONGRESS_MEMBERS'
export const SELECT_CONGRESS_MEMBER = 'SELECT_CONGRESS_MEMBER'
export const SELECT_STATE = 'SELECT_STATE'

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
        congressMembers: json.filter((t) => t.state === state) // this should probably happen on the reducer
        // also need to make use of a selector instead of making the request all the time
    }
}

export function selectCongressMember(memberId) {
    return {
        type: SELECT_CONGRESS_MEMBER,
        memberId
    }
}
