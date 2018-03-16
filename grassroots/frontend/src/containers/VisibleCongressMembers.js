import {connect} from 'react-redux';
import PropTypes from 'prop-types'
import CongressSideBar from '../components/CongressSideBar'

const mapStateToProps = ({congressMembers}) => {
    return ({congressMembers})
}

const VisibleCongressMembers = connect(
    mapStateToProps
)(CongressSideBar)

export default VisibleCongressMembers;
