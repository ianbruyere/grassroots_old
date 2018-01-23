import { call, put, takeLatest, takeEvery, all } from 'redux-saga/effects'
import { fetchSenatorData } from '../services/api'


function *getSenators(action) {
    const senateData = yield call(fetchSenatorData);
    console.log(senateData)
}


// function *watchEveryFilterCongress() {
//     yield takeEvery('FILTER_BY_STATE', getSenators)
// }

export default function *rootSaga() {
    yield all([
        yield takeEvery('FILTER_BY_STATE', getSenators)
    ])
}
