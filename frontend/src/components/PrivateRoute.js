//https://github.com/ronaksonigara/react-private-public-route/blob/main/src/components/PrivateRoute.js
import React from "react";
import { Route, Redirect } from "react-router-dom";
/*import PropTypes from "prop-types";

const propTypes = {
	isAuthenticated: PropTypes.bool,
	component: PropTypes.func.isRequired,
	redirect: PropTypes.string,
	restricted: PropTypes.bool,
};

const defaultProps = {
	restricted: false,
	redirect: "/login",
	isAuthenticated: false,
};
*/
const PrivateRoute = ({
	isAuthenticated,
	component: Component,
	redirect: pathname,
	restricted,
	...rest
}) => {
	console.log('isAuthenticated: '+isAuthenticated);
	return (
		<Route
			{...rest}
			render={(props) =>
				isAuthenticated && !restricted ? (
					<Component {...props} />
				) : (
					<Redirect to={{ pathname }} />
				)
			}
		/>
	);
};

//PrivateRoute.propTypes = propTypes;
//PrivateRoute.defaultProps = defaultProps;

export default PrivateRoute;