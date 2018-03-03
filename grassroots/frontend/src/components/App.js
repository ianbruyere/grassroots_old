import React, { Component } from 'react';
import PropTypes from 'prop-types'
import VisibleCongressMembers from '../containers/VisibleCongressMembers';
import  '../styles/App.css';
import USMAP from './USMAP';
import Header from './Header';
import Footer from './Footer';

class App extends Component {
<<<<<<< HEAD
  constructor() {
    super()
    this.state = {
      senateMembers: [],
      houseMembers:[],
      currentState: []
    }
  }
  
  componentWillMount() {
    axios.get("http://127.0.0.1:8000/api/congressmembers/")
    .then(res => {
      this.setState({
        congressMembers: res.data
      })
    })
  }
=======
>>>>>>> experiment

  render() {
    return (
      <div>
        <Header />
        <div className="wrapper">
          <article className="main">
<<<<<<< HEAD
            <USMAP congressMembers={this.state.congressMembers}/>
          </article>
          <aside className="aside aside2">   
            <CongressSideBar congressMembers={this.state.congressMembers}/>
=======
            <USMAP />
          </article>
          <aside className="aside aside2">   
            <VisibleCongressMembers />
>>>>>>> experiment
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
