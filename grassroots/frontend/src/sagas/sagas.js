import { call, put, takeLatest, takeEvery, all } from 'redux-saga/effects'
import { fetchCongressData } from '../services/api'


function *getCongressMembers(action) {
    const congressData = yield call(fetchCongressData);
}


// function *watchEveryFilterCongress() {
//     yield takeEvery('FILTER_BY_STATE', getCongressMembers)
// }

export default function *rootSaga() {
    yield all([
        yield takeEvery('FILTER_BY_STATE', getCongressMembers)
    ])
}
