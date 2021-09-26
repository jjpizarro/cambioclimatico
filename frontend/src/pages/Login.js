import React, {useState,useContext} from 'react';
import '../css/Login.css';
import authService from '../services/auth.service';
import {useHistory } from 'react-router-dom';
import {AuthContext} from '../context/Auth'
export default function Login(){
    let history = useHistory();
    const initialFormState = {
        username:null,
        password: null,
        isSubmitting:false,
        errorMessage: null
    }
    const [formData, setFormData] = useState(initialFormState);
    const { login } = useContext(AuthContext)

    const handleInputChange = ev =>{
        setFormData(
           {
               ...formData,
               [ev.target.name]:ev.target.value
           } 
        );
    }
    const handleFormSubmit = ev =>{
        ev.preventDefault();
        setFormData(
            {
                ...formData,
                isSubmitting:true
            } 
         );
         authService.login(formData.username, formData.password)
         .then(
             (data)=>{
                 login(data);
                setFormData(
                    {
                        ...formData,
                        isSubmitting:false
                    } 
                 );
                 history.push("/");
                //window.location.reload();
             },(error)=>{
                setFormData(
                    {
                        ...formData,
                        isSubmitting:false,
                        errorMessage:'Usuario y/o Contraseña incorrectos'
                    } 
                 );
             }
         );
    };

    return (
        
    <section class="my-login-page h-100">
		<div className="container h-100">
			<div className="row justify-content-md-center h-100">
				<div className="card-wrapper">
					<div className="brand">
                        <svg xmlns="http://www.w3.org/2000/svg" width="90" height="90" fill="currentColor" className="bi bi-broadcast" viewBox="0 0 16 16">
                            <path d="M3.05 3.05a7 7 0 0 0 0 9.9.5.5 0 0 1-.707.707 8 8 0 0 1 0-11.314.5.5 0 0 1 .707.707zm2.122 2.122a4 4 0 0 0 0 5.656.5.5 0 1 1-.708.708 5 5 0 0 1 0-7.072.5.5 0 0 1 .708.708zm5.656-.708a.5.5 0 0 1 .708 0 5 5 0 0 1 0 7.072.5.5 0 1 1-.708-.708 4 4 0 0 0 0-5.656.5.5 0 0 1 0-.708zm2.122-2.12a.5.5 0 0 1 .707 0 8 8 0 0 1 0 11.313.5.5 0 0 1-.707-.707 7 7 0 0 0 0-9.9.5.5 0 0 1 0-.707zM10 8a2 2 0 1 1-4 0 2 2 0 0 1 4 0z"/>
                          </svg>
                    </div>
					<div className="card fat">
						<div className="card-body">
							<h4 className="card-title">Ingresar</h4>
							<form method="POST" onSubmit={handleFormSubmit} className="my-login-validation" novalidate="">
								<div className="form-group">
									<label for="email">Correo electrónico</label>
									<input id="email" type="email" className="form-control" name="username" value={formData.username} required autofocus onChange={handleInputChange}/>
									<div className="invalid-feedback">
										Email is invalid
									</div>
								</div>

								<div className="form-group">
									<label for="password">Contraseña
									</label>
									<input id="password" type="password" className="form-control" name="password" required data-eye value={formData.password} onChange={handleInputChange}/>
								    <div className="invalid-feedback">
								    	Password is required
							    	</div>
								</div>

								

								<div className="form-group m-1">
									<button type="submit" className="w-100 btn btn-lg btn-primary">
										Login
									</button>
								</div>
								{formData.errorMessage && (<div className="form-group">
                        <div className="alert alert-danger" role="alert">
                            {formData.errorMessage}
                        </div>
                    </div>)}
							</form>
						</div>
					</div>
					<div class="footer">
						&copy; 2021 &mdash; Cambio climático 
					</div>
				</div>
			</div>
		</div>
       </section>
    );
}