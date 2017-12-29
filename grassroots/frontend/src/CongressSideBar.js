import React from 'react'
import CongressMember from './CongressMember'
import styles from './styles/CongressSideBar.css'

class CongressSideBar extends React.Component {
    render() {
        const {senateMembers} = this.props
        return (
              <ul className="listOfMembers">
              {
                  Object
                  .keys(senateMembers)
                  .map(key => 
                    <CongressMember 
                      key={key}
                      member={senateMembers[key]}/>
                  )
              }
              </ul>
        )
    }
}

export default CongressSideBar;