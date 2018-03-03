import axios from 'axios'

<<<<<<< HEAD
export function fetchCongressData() {
    return axios.get("http://127.0.0.1:8000/api/congressmembers/")  
=======

export function fetchSenatorData() {
    return axios.get("http://127.0.0.1:8000/api/congressmembers/")
    .then(res => res.data)
>>>>>>> experiment
}
