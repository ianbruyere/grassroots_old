import { combineReducers } from 'redux'
import {
    REQUEST_CONGRESS_MEMBERS,
    RECIEVE_CONGRESS_MEMBERS,
    SELECT_STATE
} from '../actions/index'

function selectedState(state = '', action) {
    switch (action.type) {
        case SELECT_STATE:
          return action.state
        default:
          return state
    }
}

function congressMembers(
    state = {
    isFetching: false,
    didInvalidate: false,
    items: []
    }, 
    action) 
    {
    switch(action.type) {
        case REQUEST_CONGRESS_MEMBERS:
        return Object.assign({}, state, {
            isFetching: true,
            didInvalidate: false
        })
        case RECIEVE_CONGRESS_MEMBERS:
          return Object.assign({}, state, {
              isFetching: false,
              didInvalidate: false,
              items: action.congressMembers
          })
        default:
            return state
    }
}

function postsBySenateMembers(state = {}, action) {
    switch (action.type) {
        case REQUEST_CONGRESS_MEMBERS:
        case RECIEVE_CONGRESS_MEMBERS:
          return Object.assign({}, state, {
              congressMembers: action.congressMembers//.filter(t => t.state===action.state)
          })
        default:
          return state
    }
}

const rootReducer = combineReducers({
    postsBySenateMembers,
    selectedState
})

export default rootReducer