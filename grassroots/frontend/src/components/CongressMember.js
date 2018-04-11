// Reacty stuff
import React from 'react'
import PropTypes from 'prop-types'
import { withRouter } from 'react-router-dom'

// Icons and Styles
import Twitter  from '../icons/Twitter'
import Facebook from '../icons/Facebook'
import Youtube from '../icons/Youtube'
import Profile from './Profile'
import '../styles/CongressMembers.css'

class CongressMember extends React.Component {
    constructor(props) {
      super(props)
      this.handleClick = this.handleClick.bind(this)
    }

    handleClick(e) {
      this.props.history.push(`/congressmember/${e.target.id}`);
    }

    render() {
        const {member} = this.props;
        return (
                <li>
                  <div className="totalListItemWrapper">
                    <div className="profileImageWrapper"><Profile /></div>
                    <div className="profileInfoWrapper">
                      <h3 id={`${member.id}`} onClick={ e => this.handleClick(e)} className={`profileInfo member-name ${member.party}`}>
                        {member.first_name} {member.last_name}
                      </h3>
                      <div className="profileInfo state">
                        { member.state }
                      </div>
                      <div className="profileInfo personal-website">
                        <a href={ member.url }>Personal Website</a>
                      </div>
                    </div>
                    <div className="socialMediaWrapper">
                      <div className="socialMedia twitter">
                        <a href={`http://www.twitter.com/${ member.twitter_account }`} 
                        alt="Twitter Feed"><Twitter fill="#76A9EA"/></a>
                      </div>
                      <div className="socialMedia facebook">
                        <a href={`http://www.facebook.com/${member.facebook_account}`} 
                        alt="Facebook Account">
                          <Facebook />
                        </a>
                      </div>
                      <div className="socialMedia youtube">
                        <a href={`http://www.youtube.com/${ member.youtube_account }`} 
                        alt="YouTube Account">
                          <Youtube />
                        </a>
                      </div>
                    </div>
                  </div>
                </li>
            )
    }
}

CongressMember.propTypes = {
    member: PropTypes.object.isRequired
}
 
export default withRouter(CongressMember);