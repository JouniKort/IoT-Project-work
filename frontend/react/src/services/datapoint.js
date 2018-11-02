import axios from 'axios'
const baseUrl = '/api/data'

const getLatest = () => axios.get(baseUrl+'/latest').then(res => res.data)

export default {getLatest}