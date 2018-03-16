import axios from 'axios'


export function fetchCongressData() {
    // going to need to make these https at some point
    return axios.get("http://127.0.0.1:8000/api/congressmembers/") 
    .then(res => res.data)
}

export function fetchSelectCongressMemberData(memberId) {
    return axios.get(`http://127.0.0.1:8000/api/congressmembers/?member_id=${memberId}`)
    .then(res => res.data)
}

export function fetchBill(url) {
    return axios.get(url).then(res => res.data)
}
