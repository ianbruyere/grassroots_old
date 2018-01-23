import React from 'react'
import PropTypes from 'prop-types'
import CongressMember from './CongressMember'
import styles from '../styles/CongressSideBar.css'

const getVisibleCongressMembers = (
    congressMembers,
    filter
) => {
    return congressMembers.filter(
        t => t.state == filter
    )
}

class CongressSideBar extends React.Component {
    constructor() {
        super();

    }
    render() {
        const visibleCongressMembers = getVisibleCongressMembers(
            this.props.senateMembers,
            "OH"
        );
        
        return (
              <ul className="listOfMembers">
                <h3>Senators</h3>
              {
                  Object
                  .keys(visibleCongressMembers)
                  .map(key => 
                    <CongressMember 
                      key={key}
                      member={visibleCongressMembers[key]}/>
                  )
              }
              </ul>
        )
    }
}

CongressSideBar.propTypes = {
    
}

export default CongressSideBar;