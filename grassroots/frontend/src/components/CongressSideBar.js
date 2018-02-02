import React from 'react'
import PropTypes from 'prop-types'
import CongressMember from './CongressMember'
import '../styles/CongressSideBar.css'

const CongressSideBar = ({congressMembers}) => (

    <ul className="listOfMembers">
        <h3>Senators</h3>
           {
               Object
               .keys(congressMembers)
               .map(key => 
                <CongressMember 
                    key={key}
                    member={congressMembers[key]}/>
                )
            }            
    </ul>
)

export default CongressSideBar;