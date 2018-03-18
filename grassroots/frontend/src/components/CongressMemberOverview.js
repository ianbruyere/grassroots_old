// Reacty Stuff
import React from 'react'
import PropTypes from 'prop-types'

// Components
import CongressMemberVotePositions from './CongressMemberVotePositions'
import VisibleBills from '../containers/VisibleBills'
import CongressMemberProfile from './CongressMemberProfile'

import '../styles/CongressMemberOverview.css'

class CongressMemberOverview extends React.Component {
    render() {
        const {selectedCongressMember} = this.props;
        // need to add some error handling
        if(selectedCongressMember.isFetching) {
            return (<div><h3>Loading...</h3></div>)
        } else { 
        return (
            <div id='OverviewWrapper'>
                <div id="CongressMemberProfile" className="infoBlock">
                  <CongressMemberProfile />
                </div>
                <div id="CongressMemberVotePositions" className="infoBlock">
                  <CongressMemberVotePositions member={selectedCongressMember.items[0]}/>
                </div>
                <div id="CongressMemberBills" className="infoBlock">
                  <VisibleBills listOfBills={selectedCongressMember.items[0].sponsoredbills}/>
                </div> 
            </div>
          )
        }
    }
}

export default CongressMemberOverview;