//Gabriel Goldstein gjg180000
//megan tran mjt170002
//jaeseonglee, jxl115330
//Yibp Li
import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import App from "./Components/App/App.js";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter as Router } from "react-router-dom";

ReactDOM.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>,
  document.getElementById("root")
);
