import React, { Component } from 'react';
import axios from 'axios';
import CongressSideBar from './CongressSideBar';
import styles from '../styles/App.css';
import USMAP from './USMAP';
import Header from './Header';
import Footer from './Footer';

class App extends Component {
  constructor() {
    super()
    this.state = {
      senateMembers: [],
      houseMembers:[],
      currentState: []
    }
  }
  
  componentWillMount() {
    axios.get("http://127.0.0.1:8000/api/senatemembers/")
    .then(res => {
      this.setState({
        senateMembers: res.data
      })
    })
  }

  render() {
    return (
      <div>
        <Header />
        <div className="wrapper">
          <article className="main">
            <USMAP senateMembers={this.state.senateMembers}/>
          </article>
          <aside className="aside aside2">   
            <CongressSideBar senateMembers={this.state.senateMembers}/>
          </aside>  
        </div>
        <Footer />
      </div>
    );
  }
}

App.propTypes = {
  
}

export default App;
