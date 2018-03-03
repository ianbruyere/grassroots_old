import axios from 'axios'

export function fetchCongressData() {
    return axios.get("http://127.0.0.1:8000/api/congressmembers/")  
}
