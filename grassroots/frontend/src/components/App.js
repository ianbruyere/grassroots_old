import React, { Component } from 'react';
import PropTypes from 'prop-types'
import VisibleCongressMembers from '../containers/VisibleCongressMembers';
import  '../styles/App.css';
import USMAP from './USMAP';
import Header from './Header';
import Footer from './Footer';

class App extends Component {

  render() {
    return (
      <div>
        <Header />
        <div className="wrapper">
          <article className="main">
            <USMAP />
          </article>
          <aside className="aside aside2">   
            <VisibleCongressMembers />
          </aside>  
        </div>
        <Footer />
      </div>
    );
  }
}

App.propTypes = {
  
}

App.contextTypes = {
  store: PropTypes.object
}
export default App;
