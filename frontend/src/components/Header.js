import React, {useContext} from "react";
import { AuthContext }  from '../context/Auth';
import {useHistory } from 'react-router-dom';

const Header = ()=>{
  let history = useHistory();
  const { logout,isAuthenticated } = useContext(AuthContext)
  const close = ()=>{
    logout();
    history.push("/");
  }
    return (
        <>
        <header>
          <div className="d-flex flex-column flex-md-row align-items-center pb-1 mb-2 border-bottom border-1">
            <span className="d-flex align-items-center text-dark text-decoration-none">
              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" fill="currentColor" className="bi bi-broadcast" viewBox="0 0 16 16">
                <path d="M3.05 3.05a7 7 0 0 0 0 9.9.5.5 0 0 1-.707.707 8 8 0 0 1 0-11.314.5.5 0 0 1 .707.707zm2.122 2.122a4 4 0 0 0 0 5.656.5.5 0 1 1-.708.708 5 5 0 0 1 0-7.072.5.5 0 0 1 .708.708zm5.656-.708a.5.5 0 0 1 .708 0 5 5 0 0 1 0 7.072.5.5 0 1 1-.708-.708 4 4 0 0 0 0-5.656.5.5 0 0 1 0-.708zm2.122-2.12a.5.5 0 0 1 .707 0 8 8 0 0 1 0 11.313.5.5 0 0 1-.707-.707 7 7 0 0 0 0-9.9.5.5 0 0 1 0-.707zM10 8a2 2 0 1 1-4 0 2 2 0 0 1 4 0z"/>
              </svg>
              <span className="fs-4 px-1">Cambio Climático</span>
            </span>
      
            <nav className="d-inline-flex mt-2 mt-md-0 ms-md-auto">
             
             { isAuthenticated?(<a href="/#"className="py-2 text-dark" onClick={close}>Cerrar sesión</a>):(<></>)
             } 
          </nav>
          </div>
      
          
        </header>
    </>
    );
}
export default Header;