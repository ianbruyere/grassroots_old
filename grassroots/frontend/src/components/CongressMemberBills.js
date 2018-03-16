import React from 'react'
import BillItem from './BillItem'
import '../styles/CongressMemberBills.css'

class CongressMemberBills extends React.Component {
    render() {
        const {member} = this.props;    
             return(
                <ul>
                   {
                       Object
                       .keys(member.sponsoredbills)
                       .map(key =>
                       <BillItem 
                          key={key}
                          bill={member.sponsoredbills[key]} /> 
                        )
                    }    
                </ul>
               )
         }
    }


export default CongressMemberBills;