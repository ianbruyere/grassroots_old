import { call, put, takeEvery, takeLatest } from 'redux-saga/effects'
import { fetchSenatorData } from '../services/api'
import {recieveCongressMembers} from '../actions/index'

function *fetchCongress(action) {
    try {
        const congressMembers = yield call(fetchSenatorData)
        yield put(recieveCongressMembers(action.state, congressMembers));
    } catch(e) {
        yield put({type:"REQUEST_CONGRESS_MEMBERS_FAILED", message: e.message})
    }
}

export default function *mySaga() {
    yield takeEvery("REQUEST_CONGRESS_MEMBERS", fetchCongress)
}
