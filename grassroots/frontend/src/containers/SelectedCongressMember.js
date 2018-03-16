import {connect} from 'react-redux';
import PropTypes from 'prop-types'
import CongressMemberOverview from '../components/CongressMemberOverview'

const mapStateToProps = ({selectedCongressMember}) => {
    return ({selectedCongressMember})  
}

const SelectedCongressMember = connect(
    mapStateToProps
)(CongressMemberOverview)

export default SelectedCongressMember;