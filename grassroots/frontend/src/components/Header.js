import React from 'react';
import styles from '../styles/Header.css';

class Header extends React.Component {
    render() {
        return (
        <ul className="navigation">
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Forum</a></li>
          <li><a href="#">Contact</a></li>
          <li className="right"><a href="#">Login</a></li>
          <li className="right"><a href="#">Sign Up</a></li>
        </ul>
    )
    }
}

export default Header;