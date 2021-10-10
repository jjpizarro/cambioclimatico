export const AuthReducer = (state, action)=>{
    switch(action.type){
        case 'LOGIN':
            return {
                ...state,
                isAuthenticated:true,
                user:action.payload
            };
        case 'LOGOUT':
            localStorage.clear();
            return {
                ...state,
                isAuthenticated:false,
                user:null
            }

    }
}
