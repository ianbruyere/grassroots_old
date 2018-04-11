import { connect } from 'react-redux';
import PropTypes from 'prop-types'
import { requestBill } from '../actions/index'
import CongressMemberBills from '../components/CongressMemberBills'

const mapStateToProps = (state, ownProps) => {
    return {
        bills: state.bills,
        listOfBills: ownProps.listOfBills
    }
}

const mapDispatchToProps = (dispatch) => {
   return {
       requestBill: billURL => {
           dispatch(requestBill(billURL))
       }
   }
}

const VisibleBills = connect(
    mapStateToProps
)(CongressMemberBills)

export default VisibleBills;