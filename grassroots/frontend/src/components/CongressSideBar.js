import React from 'react'
import PropTypes from 'prop-types'
import CongressMember from './CongressMember'
import '../styles/CongressSideBar.css'

const CongressSideBar = ({congressMembers}) => (
        // so basically right now when I click on a state,
        // I need to make a call to the api, nab the senate members,
        // than populate the side bar with ONLY the members that are part
        // of that state. 
        //currently my middleware will make the call to the api

    <ul className="listOfMembers">
    {console.log(congressMembers)}
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

// CongressSideBar.propTypes = {
//     congressMembers: PropTypes.arrayOf(
//         PropTypes
//     )
// }


export default CongressSideBar;