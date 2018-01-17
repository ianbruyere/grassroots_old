import { combineReducers } from 'redux'
import { filterCongressBar } from '../actions'

const initialState = {
   
}

const getVisibleCongressMembers = (
    congressMembers,
    filter
) => {
    return congressMembers.filter(
        t => t.state == filter
    )
}

function congressBarFilter(state = initialState, action) {
    switch (action.type) {
        case "FILTER_BY_STATE":
            return action.state
        default:
            return state
    }
}

const congressApp = combineReducers({
    congressBarFilter
})

export default congressApp;