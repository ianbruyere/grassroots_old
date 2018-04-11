import React from 'react';
import PropTypes from 'prop-types'
import VisibleCongressMembersList from '../containers/VisibleCongressMembersList';
import  '../styles/App.css';
import VisibleUSMap from '../containers/VisibleUSMap';
import Header from './Header';
import Footer from './Footer';

const App = () => 
 (
      <div>
        <Header />
        <div className="wrapper">
          <article className="main">
            <VisibleUSMap />
          </article>
            
            <VisibleCongressMembersList  />
 
        </div>
        <Footer />
      </div>
)

export default App;
