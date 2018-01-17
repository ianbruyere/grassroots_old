import React from 'react';
import {filterCongressBar} from '../actions/index'
import PropTypes from 'prop-types';



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
        const { store } = this.context;
        store.dispatch(filterCongressBar(e.target.id));
        // this.setState({ stateClicked : e.target.id });
        // this.props.callBackParent(e.target.id); // notify of change
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
              fill="#ffffff"/>
            </g>
            
        )
    }
}

State.propTypes = {
    state: PropTypes.string.isRequired,
    key: PropTypes.string.isRequired
}

State.contextTypes = {
    store: PropTypes.object
}

export default State;