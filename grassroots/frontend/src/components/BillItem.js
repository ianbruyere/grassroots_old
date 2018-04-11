import React from 'react'
import PropTypes from 'prop-types'

class BillItem extends React.Component {
    render() {
        const {bill} = this.props;
        if(!bill) {
            return (<h3>Loading...</h3>)
        } else {
        return(
            <li>
                <div className="totalLisItemWrapper">
                  <div className="billInfoWrapper" >
                    <b>{bill.bill.short_title}</b>
                  </div>
                </div>
              
            </li>
        )
      }
    }
}

export default BillItem;