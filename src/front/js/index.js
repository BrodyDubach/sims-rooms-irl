//import react into the bundle
import React from "react";
import ReactDOM from "react-dom";

//include your index.scss file into the bundle
import "../styles/index.css";
import "../styles/navbar.css";
import "../styles/home.css";
import "../styles/room.css";
import "../styles/list.css";
import "../styles/user.css";
import"../styles/search.css";
//import your own components
import Layout from "./layout";
	



//render your react application
ReactDOM.render(<Layout />, document.querySelector("#app"));
