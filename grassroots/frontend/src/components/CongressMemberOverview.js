// Reacty Stuff
import React from 'react'
import PropTypes from 'prop-types'

// Components
import CongressMemberVotePositions from './CongressMemberVotePositions'
import CongressMemberBills from './CongressMemberBills'
import CongressMemberProfile from './CongressMemberProfile'

import '../styles/CongressMemberOverview.css'

class CongressMemberOverview extends React.Component {
    render() {
        console.log(this.props);
        const {selectedCongressMember} = this.props;
        // need to add some error handling
        if(selectedCongressMember.isFetching) {
            return (<div><h3>Loading...</h3></div>)
        } else { 
        return (
            <div id='OverviewWrapper'>
                <div id="CongressMemberProfile" className="infoBlock">
                </div>
                <div id="CongressMemberVotePositions" className="infoBlock">
                  <CongressMemberVotePositions member={selectedCongressMember.items[0]}/>
                </div>
                <div id="CongressMemberBills" className="infoBlock">
                  <CongressMemberBills member={selectedCongressMember.items[0]}/>
                </div> 
            </div>
          )
        }
    }
}

export default CongressMemberOverview;