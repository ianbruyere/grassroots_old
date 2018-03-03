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
    axios.get("http://127.0.0.1:8000/api/congressmembers/")
    .then(res => {
      this.setState({
        congressMembers: res.data
      })
    })
  }

  render() {
    return (
      <div>
        <Header />
        <div className="wrapper">
          <article className="main">
            <USMAP congressMembers={this.state.congressMembers}/>
          </article>
          <aside className="aside aside2">   
            <CongressSideBar congressMembers={this.state.congressMembers}/>
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
