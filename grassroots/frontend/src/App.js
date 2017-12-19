import React, { Component } from 'react';
import axios from 'axios';
import './App.css';

class App extends Component {
  constructor() {
    super()
    this.onClick = this.onClick.bind(this)
  }
  onClick(ev) {
    console.log("Sending a GET API Call !!!!")
    axios.get('http://127.0.0.1:8000/api/senatemembers/')
    .then(res => {
      console.log(res)
    }).then(response => {
      console.log(JSON.stringify(response))
    })
  }
  render() {
    return (
      <div>
        <button type="button" onClick={this.onClick}>Send GET /senatemembers</button>
      </div>
    );
  }
}

export default App;
