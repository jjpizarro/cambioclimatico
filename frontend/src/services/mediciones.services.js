import http from './http-common';

const getMediciones = () =>{
    return http.get('/mediciones')
}
const getMedicion = id => {
    return http.get(`/mediciones/${id}`)
}
const updateMedicion = (data) =>{
    return http.put('/mediciones',data);
}
const getEstaciones = () =>{
    return http.get('/estaciones');
}
const getParametros = () =>{
    return http.get('/parametros');
}
const filtrarBusqueda = (data) =>{
    console.log(data);
    return http.post('/filtros',data);
}
export default {
    getMediciones,
    getMedicion,
    updateMedicion,
    getEstaciones,
    getParametros,
    filtrarBusqueda
}