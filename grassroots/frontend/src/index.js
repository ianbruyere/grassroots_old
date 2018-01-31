// General Reacty things
import React from 'react';
import ReactDOM from 'react-dom';
import registerServiceWorker from './registerServiceWorker';
import { BrowserRouter, Switch, Route } from 'react-router-dom'

// Redux stuff
import { Provider } from 'react-redux'
import rootReducer from './reducers/index'
import { createStore, applyMiddleware } from 'redux'

// Saga Middleware
import createSagaMiddleware from 'redux-saga'
import mySaga from './sagas/sagas'


// Components and whatnot
import './styles/index.css';
import App from './components/App';
import NotFound from './components/NotFound';


const sagaMiddleware = createSagaMiddleware()

const store = createStore(
  rootReducer,
  applyMiddleware(sagaMiddleware)
);

sagaMiddleware.run(mySaga)

const Root = () => {
  return (
  <Provider store={store}>
    <BrowserRouter>
      <Switch>
        <Route exact path="/" component={App} />
        <Route path="*" component={NotFound} /> 
      </Switch>
    </BrowserRouter>
  </Provider>
  )
}

ReactDOM.render(<Root/>, document.getElementById('root'))

registerServiceWorker();
