import React from 'react'

class SenateMember extends React.Component {

    render() {
        const {member} = this.props
        return (
            <div className="senate-member">
                <li className="senate-member">
                  <h3 className="member-name">
                    {member.first_name} {member.last_name}
                  </h3>
                  <div className="twitter">{ member.twitter_account }</div>
                  <div className="facebook">{member.facebook_account}</div>
                  <div className="youtube">{ member.youtube_account }</div>
                  <div className="state">{ member.state }</div>
                  <div className="personal-website">{ member.url }</div>
                </li>
            </div>
            )
    }
}

SenateMember.propTypes = {
    //member: React.PropTypes.object.isRequired
}
export default SenateMember;