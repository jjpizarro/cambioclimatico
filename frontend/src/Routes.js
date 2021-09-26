import React, {useContext} from 'react'
import {Switch} from "react-router-dom"
import Mediciones from './pages/Mediciones'
import Login from './pages/Login';
import PublicRoute from './components/PublicRoute';
import PrivateRoute from './components/PrivateRoute';
import { AuthContext }  from './context/Auth'

export default function Routes(){
    const { isAuthenticated } = useContext(AuthContext)
    return (
        <Switch>
             <PublicRoute exact path="/login" component={Login} />
             <PrivateRoute exact path="/" 
             isAuthenticated={isAuthenticated}
             redirect="/login"
             component={Mediciones} />
       </Switch>     
       
    )
}