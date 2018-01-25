import React from 'react'
import PropTypes from 'prop-types'
import styles from '../styles/CongressMembers.css'
import Twitter  from '../icons/Twitter'
import Facebook from '../icons/Facebook'
import Youtube from '../icons/Youtube' // Really dont know what value Youtube provides
import Profile from './Profile'


class CongressMember extends React.Component {

    render() {
        const {member} = this.props;
        return (
                <li>
                  <div className="totalListItemWrapper">
                    <div className="profileImageWrapper"><Profile /></div>
                    <div className="profileInfoWrapper">
                      {/* <h3 className={`profileInfo member-name ${member.party}`}>
                        {member.first_name} {member.last_name}
                      </h3> */}
                      <h3 className="profileInfo member-name">
                        {member.first_name} {member.last_name}
                      </h3>
                      <div className="profileInfo state">{ member.state }</div>
                      <div className="profileInfo personal-website"><a href={ member.url }>Personal Website</a></div>
                    </div>
                    <div className="socialMediaWrapper">
                      <div className="socialMedia twitter">
                        <a href={`http://www.twitter.com/${ member.twitter_account }`} 
                        alt="Twitter Feed"><Twitter fill="#76A9EA"/></a>
                      </div>
                      <div className="socialMedia facebook">
                        <a href={`http://www.facebook.com/${member.facebook_account}`} alt="Facebook Account"><Facebook /></a>
                      </div>
                      <div className="socialMedia youtube">
                        <a href={`http://www.youtube.com/${ member.youtube_account }`} alt="YouTube Account"><Youtube /></a>
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
export default CongressMember;