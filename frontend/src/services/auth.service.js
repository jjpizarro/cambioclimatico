import axios from "axios";
const http = axios.create({
    baseURL: process.env.REACT_APP_ENDPOINT
  });

const register = (username, email, password)=>{
    return http.post('/signup',{username, email, password});
}

const login = (username, password)=>{
    return http.post('/login',JSON.stringify(`grant_type=&username=${username}&password=${password}&scope=&client_id=&client_secret=`),{
        
          "Content-type": "application/x-www-form-urlencoded"
        }).then((response)=>{
        if(response.data.access_token){
            localStorage.setItem('user',JSON.stringify(response.data));
        }
        return response.data;
    });
}
const logout =()=>{
    localStorage.removeItem('user');
}

const getCurrentUser = ()=>{
    return JSON.parse(localStorage.getItem('user') );
}

export default {
    register,
    login,
    logout,
    getCurrentUser
}