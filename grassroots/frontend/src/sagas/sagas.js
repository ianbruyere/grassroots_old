import { call, put, takeEvery, takeLatest } from 'redux-saga/effects'
import { fetchCongressData, fetchSelectCongressMemberData, fetchBill } from '../services/api'
import {recieveCongressMembers, recieveSelectCongressMember, recieveBill} from '../actions/index'

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
        const selectCongressMember = yield call(fetchSelectCongressMemberData, action.memberId)
        yield put(recieveSelectCongressMember(selectCongressMember));
    } catch(e) {
        yield put({type: "SELECT_CONGRESS_MEMBER_FAILED", message: e.message})
    }
}

function *fetchtheBill(action) {
    try {
       const bill = yield call(fetchBill, action.url)
       yield put(recieveBill(bill))
    } catch(e) {
        yield put({type: "REQUEST_BILL_FAILED",  message: e.message})
    }
}

export default function *mySaga() {
    yield takeEvery("REQUEST_CONGRESS_MEMBERS", fetchCongress)
    yield takeEvery("SELECT_CONGRESS_MEMBER", fetchCongressMember)
    yield takeEvery("REQUEST_BILL", fetchtheBill )
}
