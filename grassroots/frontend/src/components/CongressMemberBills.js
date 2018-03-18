import React from 'react'
import PropTypes from 'prop-types'
import BillItem from './BillItem'
import {requestBill} from '../actions/index'
import '../styles/CongressMemberBills.css'

class CongressMemberBills extends React.Component {
    componentWillMount() {
        const {store} = this.context;
        const {listOfBills} = this.props;
        listOfBills.forEach(bill => {
            store.dispatch(requestBill(bill))
        });
    }
    render() {
        const {bills} = this.props;  
             return(
                <ul>
                    {Object
                    .keys(bills.items)
                    .map(key => 
                    <BillItem bill={bills.items[key]} />
                )}
                </ul>
               )
         }
      
    }



CongressMemberBills.contextTypes = {
    store: PropTypes.object
}
export default CongressMemberBills;