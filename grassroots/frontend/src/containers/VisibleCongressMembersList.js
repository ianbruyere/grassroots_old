import {connect} from 'react-redux';
import PropTypes from 'prop-types'
import CongressSideBar from '../components/CongressSideBar'

const mapStateToProps = ({congressMembers}) => {
    return {
        active: congressMembers.length > 0,
        congressMembers
    }
}

const VisibleCongressMembersList = connect(
    mapStateToProps
)(CongressSideBar)

export default VisibleCongressMembersList;
