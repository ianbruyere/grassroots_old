import {connect} from 'react-redux';
import PropTypes from 'prop-types'
import CongressSideBar from '../components/CongressSideBar'

const mapStateToProps = state => {
    return {
        congressMembers: state.postsBySenateMembers.congressMembers ? state.postsBySenateMembers.congressMembers : []
    }
}


const VisibileCongressMembers = connect(
    mapStateToProps
)(CongressSideBar)


export default VisibileCongressMembers;