import { call, put, takeEvery, takeLatest } from 'redux-saga/effects'
import { fetchCongressData } from '../services/api'
import {recieveCongressMembers} from '../actions/index'

function *fetchCongress(action) {
    try {
        const congressMembers = yield call(fetchCongressData)
        yield put(recieveCongressMembers(action.state, congressMembers));
    } catch(e) {
        yield put({type:"REQUEST_CONGRESS_MEMBERS_FAILED", message: e.message})
    }
}

function *fetchCongressMember(action) {
    try {
        const selectCongressMember = yield call(fetchSelectCongressMemberData(action.memberId))
        yield put(recieveSelectCongressMember(action, selectCongressMember));
    } catch(e) {
        yield put({type: "SELECT_CONGRESS_MEMBER_FAILED", message: e.message})
    }
}

export default function *mySaga() {
    yield takeEvery("REQUEST_CONGRESS_MEMBERS", fetchCongress)
    yield takeEvery("SELECT_CONGRESS_MEMBER", fetchCongressMember)
}
