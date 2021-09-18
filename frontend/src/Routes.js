import React from 'react'
import {Route, Switch} from "react-router-dom"
import Mediciones from './pages/Mediciones'
export default function Routes(){
    return (
        <Switch>
            <Route exact path="/" component={Mediciones} />
        </Switch>
    )
}