import React from 'react';
import PropTypes from 'prop-types';
import { selectState, requestCongressMembers } from '../actions/index'

class State extends React.Component {
    constructor() {
        super()
        this.handleClick = this.handleClick.bind(this)
    }

    handleClick(e) {
      const {store} = this.context;
      store.dispatch(requestCongressMembers(e.target.id))
    }
    render() {
        const { stateOutline, id } = this.props
        return (
            <g>
              <path 
              onClick={e => this.handleClick(e)}
              d={stateOutline} 
              id={id}
              fill="#ffffff"/>
            </g>
            
        )
    }
}

State.contextTypes = {
    store: PropTypes.object
}

export default State;