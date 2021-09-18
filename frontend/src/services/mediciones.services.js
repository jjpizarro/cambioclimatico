import http from './http-common'

const getMediciones = () =>{
    return http.get('/mediciones')
}
const getMedicion = id => {
    return http.get(`/mediciones/${id}`)
}
const updateMedicion = (data) =>{
    return http.put('/mediciones',data);
}
export default {
    getMediciones,
    getMedicion,
    updateMedicion
}