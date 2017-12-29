import React from 'react'
import styles from './styles/CongressMembers.css'


class CongressMember extends React.Component {

    render() {
        const {member} = this.props;
        return (
                <li>
                  <div className="totalListItemWrapper">
                    <div className="profileImageWrapper"></div>
                    <div className="profileInfoWrapper">
                      <h3 className={`profileInfo member-name ${member.party}`}>
                        {member.first_name} {member.last_name}
                      </h3>
                      <div className="profileInfo state">{ member.state }</div>
                      <div className="profileInfo personal-website"><a href={ member.url }>Personal Website</a></div>
                    </div>
                    <div className="socialMediaWrapper">
                      <div className="socialMedia twitter"><a href={ member.twitter_account } alt="Twitter Feed">T</a></div>
                      <div className="socialMedia facebook"><a href={member.facebook_account} alt="Facebook Account">F</a></div>
                      <div className="socialMedia youtube"><a href={ member.youtube_account } alt="YouTube Account">Y</a></div>
                    </div>
                  </div>
                </li>
            )
    }
}

CongressMember.propTypes = {
    //member: React.PropTypes.object.isRequired
}
export default CongressMember;