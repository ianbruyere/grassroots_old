import { combineReducers } from 'redux'
import {
    REQUEST_CONGRESS_MEMBERS,
    RECIEVE_CONGRESS_MEMBERS,
    SELECT_STATE,
    SELECT_CONGRESS_MEMBER,
    RECIEVE_SELECT_CONGRESS_MEMBER,
    REQUEST_BILL,
    RECIEVE_BILL
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
              items: action.congressMembers.filter((t) => t.state === action.state)
          })
        default:
            return state
    }
}

function bills(
    state = {
        isFetching: false,
        didInvalidate: false,
        items: []        
    },
    action) {
        switch(action.type){
            case REQUEST_BILL:
            return Object.assign({}, state, {
                isFetching: true,
                didInvalidate: false
            })
            case RECIEVE_BILL:
            return Object.assign({}, state, {
                isFetching: false,
                didInvalidate: false,
                items: action.bill
            })
        }
    }

function selectedCongressMember(
    state = {
        isFetching: false,
        didInvalidate: false,
        items: []
        }, 
        action) 
    {
        switch(action.type){
        case SELECT_CONGRESS_MEMBER:
        return Object.assign({}, state, {
            isFetching: true,
            didInvalidate: false,
        })
        case RECIEVE_SELECT_CONGRESS_MEMBER:
        return Object.assign({}, state, {
            isFetching: false,
            didInvalidate: false,
            items: action.congressMembers
        })
        default:
            return state   
    }
}

const rootReducer = combineReducers({
    selectedCongressMember,
    congressMembers,
    selectedState
})

export default rootReducer;