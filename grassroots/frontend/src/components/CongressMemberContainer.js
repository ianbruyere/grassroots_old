// Reacty Stuff
import React from 'react'
import PropTypes from 'prop-types'

// container
import SelectedCongressMember from '../containers/SelectedCongressMember'

// components
import Header from './Header';
import Footer from './Footer';

import '../styles/CongressMemberContainer.css'


//Redux Stuff
import { selectCongressMember } from '../actions/index'

class CongressMemberContainer extends React.Component {
  
  render() {
    const {store} = this.context;
    store.dispatch(selectCongressMember(this.props.match.params.congressMemberId));
      return (
        <div>
          <Header />  
          <div id="CongressMemberWrapper">
            <SelectedCongressMember />
          </div>
          <Footer />
       </div>
      )
    }
  }


CongressMemberContainer.contextTypes = {
    store: PropTypes.object
}      

export default CongressMemberContainer;
