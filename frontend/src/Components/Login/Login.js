import "./Login.css";
import React, { useState, useEffect } from 'react'
import axios from "axios";

function Login(props) {
    const [username, setUsername] = useState(0);
    const [password, setPassword] = useState(0);
    

    function handleLogin(e, username, password) {
      axios
      .post("http://localhost:5000/login", {
        username: username,
        password: password
      })
      .then((response) => { 
        if(response.data.msg === 'Logged in successfully !') {
            props.setLoggedIn();
        }
        else {
          console.log('Login Failed');
        }
      });
           
     
    }
  
    return (
      <div className="App">
        <header className="Login"></header>
        <form onSubmit={handleLogin}>
          <label htmlFor="username">
            <b>Username</b>
          </label>
          <input
            type="text"
            placeholder="Enter Username"
            name="username"
            required
            onChange={(e)=>setUsername(e.target.value)}
          />
          <label htmlFor="password">
            <b>Password</b>
          </label>
          <input
            type="password"
            placeholder="Enter Password"
            name="password"
            required
            onChange={(e)=>setPassword(e.target.value)}
          />
           <input type="submit" value="Submit" />
        </form>
        <div>
        Don't have an account?
        <button onClick={props.createNewAccount}>
          Create Account
            </button>
        </div>
      </div>
    );
  }
  export default Login;