import React from 'react'
import PropTypes from 'prop-types'
import CongressMember from './CongressMember'
import '../styles/CongressSideBar.css'
import '../styles/App.css'

const CongressSideBar = ({congressMembers, active}) => {
    var className = active ? 'open' : '';
    className = className + ' aside aside2' 
    return (
    <div className="container">
      <aside className="aside aside2" >     
        <ul className="listOfMembers">
            <h3>Senators</h3>
            {
                Object
                .keys(congressMembers.items)
                .map(key => 
                    <CongressMember 
                        key={key}
                        member={congressMembers.items[key]}/>
                    )
                }            
        </ul>
      </aside> 
    </div>
)}

export default CongressSideBar;