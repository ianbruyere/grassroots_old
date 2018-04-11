import React from 'react'
import PropTypes from 'prop-types'
import SelectedState from '../containers/SelectedState'
import '../styles/USMAP.css';



const USMap = ({usmap}) => (
            <div>
              <svg className="usmap" width="959" height="593" transform="translate(0 0)">
                {
                    Object
                    .keys(usmap)
                    .map(key => 
                    <SelectedState 
                    key={key}
                    id={key}
                    stateOutline={usmap[key]}
                    />)
                }
             </svg>
          </div>   
)


export default USMap;