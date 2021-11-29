import "./Login.css";
import React, { useState, useEffect } from "react";
import { Button, Form, Card } from "react-bootstrap";
import axios from "axios";

function Login(props) {
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
    <div className="AppLogin mt-5">
      <Card className="mx-auto" style={{ width: "18rem" }}>
        <Card.Header>Login</Card.Header>
        <Card.Body>
          <Form onSubmit={handleLogin}>
            <Form.Group controlId="formUsername">
              <label htmlFor="userid"></label>
              <Form.Label>Username</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter Username"
                name="userid"
                required
              />
            </Form.Group>
            <Form.Group className="mb-1" controlId="formPassword">
              <label htmlFor="password"></label>
              <Form.Label>Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter Password"
                name="password"
                required
              />
              <br></br>
            </Form.Group>

            <Button variant="success" type="submit" value="Submit">
              Submit
            </Button>
          </Form>

          <div className="mt-4">
            Don't have an account?
            <br></br>
            <Button variant="outline-primary" onClick={props.createNewAccount}>
              Create Account
            </Button>
          </div>
        </Card.Body>
      </Card>
    </div>
  );
}
export default Login;
