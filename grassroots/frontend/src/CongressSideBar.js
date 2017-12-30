import React from 'react'
import CongressMember from './CongressMember'
import styles from './styles/CongressSideBar.css'


class CongressSideBar extends React.Component {
    constructor() {
        super();

    }
    render() {
        const {senateMembers} = this.props
        return (
              <ul className="listOfMembers">
                <h3>Sentators</h3>
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