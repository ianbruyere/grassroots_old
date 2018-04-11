import React from 'react'
import PropTypes from 'prop-types'
import BillItem from './BillItem'
import '../styles/CongressMemberBills.css'

const CongressMemberBills = ({listOfBills, requestBill, bills }) => {
    listOfBills.forEach(bill => {
            requestBill(bill)
    })
    return (
            <ul>
                {Object
                .keys(bills.items)
                .map(key => 
                <BillItem bill={bills.items[key]} />
            )}
            </ul>
        )      
}
export default CongressMemberBills;