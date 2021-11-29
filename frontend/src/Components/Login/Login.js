import "./Login.css";
import React, { useState, useEffect } from "react";
import { Button, FormControl, Form } from "react-bootstrap";
import axios from "axios";

function Login(props) {
  const [username, setUsername] = useState(0);
  const [password, setPassword] = useState(0);

  function handleLogin(e, username, password) {
    e.preventDefault();
    let loginInfo = new FormData(e.target);
    props.setLoggedIn();
    console.log(loginInfo);
    /*
    axios
      .post("http://localhost:8080/login", {
        loginInfo,
      })
      .then((response) => {
        if (response.data.msg === "Successfully logged in!") {
          props.setLoggedIn();
        } else {
          console.log("Login Failed");
        }
      });
      */
  }

  return (
    <div className="App">
      <header className="Login"></header>
      <Form className="m-3" onSubmit={handleLogin}>
        {/* <label htmlFor="username">
          <b>Username</b>
        </label>
        <input
          type="text"
          placeholder="Enter Username"
          name="username"
          required
          onChange={(e) => setUsername(e.target.value)}
        />
        <label htmlFor="password">
          <b>Password</b>
        </label>
        <input
          type="password"
          placeholder="Enter Password"
          name="password"
          required
          onChange={(e) => setPassword(e.target.value)}
        />
        <input type="submit" value="Submit" /> */}

        <Form.Group className="mb-3" controlId="formUsername">
          <label for="username">Username</label>
          <input
            type="text"
            placeholder="Enter Username"
            name="username"
            required
            onChange={(e) => setUsername(e.target.value)}
          ></input>
        </Form.Group>
        <Form.Group className="mb-3" controlId="formPassword">
          <label for="password">Password</label>
          <input
            type="password"
            placeholder="Enter Password"
            name="password"
            required
            onChange={(e) => setPassword(e.target.value)}
          ></input>
          <br></br>
        </Form.Group>

        <Button variant="success" type="submit" value="Submit">
          Submit
        </Button>
      </Form>

      <div className="mt-5">Don't have an account?</div>
      <Button variant="outline-primary" onClick={props.createNewAccount}>
        Create Account
      </Button>
    </div>
  );
}
export default Login;
