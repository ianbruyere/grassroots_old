import React from 'react'
import SenateMember from './SenateMember'

class State extends React.Component {
    constructor() {
        super()
        this.onHover = this.onHover.bind(this);
    }
    onHover(e) {
        console.log(this);
    }
    render() {
        const { state, id, senateMembers } = this.props
        // console.log(filteredSenateMembers)
        return (
            <path onMouseOver={(e) => this.onHover(e)}
            d={state} 
            id={id}
            data-info={
            <div>
                <h3>Senate Members</h3> 
                {
                  Object
                  .keys(senateMembers)
                  .map(key => 
                    <SenateMember 
                      key={key}
                      member={senateMembers[key]}
                    />) 
                }   
            </div>}
            fill="#D3D3D3"/>
        )
    }
}

State.propTypes = {
    // state: React.PropTypes.string.isRequired,
    // key: React.PropTypes.string.isRequired
}

export default State;