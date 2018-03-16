import React from 'react'
import '../styles/CongressMemberVotePositions.css'


class CongressMemberVotePositions extends React.Component {
    render() {
        const {member} = this.props;
        return (
            <div><h3>{member.first_name}</h3></div>
        )
    }
}

export default CongressMemberVotePositions;