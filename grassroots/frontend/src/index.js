import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css';
import { createStore } from 'redux'
import  congressApp  from './reducers/index'
import { Provider } from 'react-redux'
import App from './components/App';
import registerServiceWorker from './registerServiceWorker';

const store = createStore(congressApp)

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>, 
  document.getElementById('root')
);
registerServiceWorker();
