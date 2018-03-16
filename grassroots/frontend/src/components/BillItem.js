import React from 'react'
import PropTypes from 'prop-types'

import {requestBill} from '../actions/index'

class BillItem extends React.Component {
    componentWillMount() {
       const {store} = this.context;
       const {bill} = this.props;
       store.dispatch(requestBill(bill))
    }
    render() {
        return(
            <li>
              <b>A Bill will go here</b>
            </li>
        )
    }
}

BillItem.contextTypes = {
    store: PropTypes.object
}
export default BillItem;