import { connect } from 'react-redux'
import { selectState, requestCongressMembers } from '../actions/index'
import PropTypes from 'prop-types'
import State from '../components/State'

const mapStateToProps = (state, ownProps) => {
    return {
        id: ownProps.id,
        stateOutline: ownProps.stateOutline,
        active: state.SelectedState === ownProps.id
    }
}

const mapDispatchToProps = (dispatch) => {
    return {
        onStateClick: id => {
            dispatch(selectState(id))
            dispatch(requestCongressMembers(id))
        }
    } 
}

const SelectedState = connect(
    mapStateToProps,
    mapDispatchToProps
)(State)

export default SelectedState;