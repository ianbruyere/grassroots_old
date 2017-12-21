import React, { Component } from 'react';
import axios from 'axios';
import SenateMember from './SenateMember'
import './App.css';
import USMAP from './USMAP'

class App extends Component {
  constructor() {
    super()
    this.state = {
      senateMembers: []
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
        {/* <h1>Senate Members</h1>
        <ul className="list-of-members">
          {
            Object
            .keys(this.state.senateMembers)
            .map(key => <SenateMember 
                 key={key} 
                 member={this.state.senateMembers[key]} 
              />)
          }
        </ul>  */}
        <USMAP senateMembers={this.state.senateMembers}/>  
      </div>
    );
  }
}

App.propTypes = {
  
}

export default App;
