import React from 'react';
import '../styles/USState.css'

const State = ({onStateClick, id, stateOutline, active}) => {
    if (active) {
        console.log('getting in the active state')
        return (
            <g transform="scale(2.0)">
              <path 
              onClick={e => onStateClick(e.target.id)}
              d={stateOutline} 
              id={id}
              fill="#ffffff"
              className="active"
              />
            </g>
            
)} else {
    return (
        <g>
        <path 
        onClick={e => onStateClick(e.target.id)}
        d={stateOutline} 
        id={id}
        fill="#ffffff"
        />
      </g>
    )
 }
}


export default State;