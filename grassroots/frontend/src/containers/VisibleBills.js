import { connect } from 'react-redux';
import PropTypes from 'prop-types'
import CongressMemberBills from '../components/CongressMemberBills'

const mapStateToProps = (state, ownProps) => {
    return {
        bills: state.bills,
        listOfBills: ownProps.listOfBills
    }
}

const mapDispatchToProps = () => {

}

const VisibleBills = connect(
    mapStateToProps
)(CongressMemberBills)

export default VisibleBills;