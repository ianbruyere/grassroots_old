import React from 'react'

class State extends React.Component {
    constructor() {
        super()
        this.handleClick = this.handleClick.bind(this)
        this.state = {
            stateClicked : '',
            senateMembers : []
        }
        // this.onHover = this.onHover.bind(this);
    }
    handleClick(e) {

        this.setState({ stateClicked : e.target.id });
        this.props.callBackParent(e.target.id); // notify of change
    }
    render() {
        const { stateOutline, id } = this.props
        return (
            <g>
              <path 
              // onMouseOver={e => this.onHover(e, senateMembers)}
              onClick={e => this.handleClick(e)}
              d={stateOutline} 
              id={id}
              fill="#808080"/>
            </g>
            
        )
    }
}

State.propTypes = {
    // state: React.PropTypes.string.isRequired,
    // key: React.PropTypes.string.isRequired
}

export default State;