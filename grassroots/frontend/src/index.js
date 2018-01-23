import React from 'react';
import ReactDOM from 'react-dom';
import './styles/index.css';
import { createStore, applyMiddleware } from 'redux'
import createSagaMiddleware from 'redux-saga'
import  congressApp  from './reducers/index'
import { Provider } from 'react-redux'
import App from './components/App';
import registerServiceWorker from './registerServiceWorker';
import  rootSaga  from './sagas/sagas'

const sagaMiddleware = createSagaMiddleware()
const store = createStore(
  congressApp,
  applyMiddleware(sagaMiddleware)
)

sagaMiddleware.run(rootSaga)

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>, 
  document.getElementById('root')
);


registerServiceWorker();
