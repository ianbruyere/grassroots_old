import { createStore, applyMiddleware, compose } from 'redux'
import rootReducer from '../reducers'
import createSagaMiddleware from 'redux-saga'

const sagaMiddleware = createSagaMiddleware()
let store = createStore(congressApp)


const configureStore = preloadedState => {
    const store = createStore(
       rootReducer,
       preloadedState,
       compose(
           applyMiddleware(sagaMiddleware)
       )
    )
}