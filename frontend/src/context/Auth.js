import React, { useReducer } from 'react'
//import PropTypes from 'prop-types'
//import authService from '../services/auth.service'
import { AuthReducer } from './authReducer'
export const AuthContext = React.createContext({})
const initialState = {
    isAuthenticated:false,
    user:null
}
export default function Auth({ children }) {
    const [state, dispatch] = useReducer(AuthReducer,initialState);
    function login (user){
        dispatch({type:'LOGIN',payload:user});
    }
    function logout(){
        dispatch({type:'LOGOUT'});
    }
    /*const [isAuthenticated, setIsAuthenticated] = useState(false)
    useEffect(() => {
        checkAuth()
    }, [])

    const checkAuth  = ()=>{
        const user = authService.getCurrentUser();
        if(user){
            setIsAuthenticated(true);
        }else{
            setIsAuthenticated(false);
        }
    }*/
    return (
        <AuthContext.Provider value={ {login,
            logout,
            ...state}}>
            {children}
        </AuthContext.Provider>
    )

}