import React from 'react';
import { Link } from 'react-router-dom'
import '../styles/Header.css';

class Header extends React.Component {
    render() {
        return (
        <ul className="navigation">
          <li><Link to='/'>Home</Link></li>
          <li><Link to='/'>About</Link></li>
          <li><Link to='/'>Forum</Link></li>
          <li><Link to='/'>Contact</Link></li>
          <li className="right"><Link to='/'>Login</Link></li>
          <li className="right"><Link to='/'>Sign Up</Link></li>
        </ul>
    )
    }
}

export default Header;