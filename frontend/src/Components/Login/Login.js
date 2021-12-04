import "./Login.css";
import React, { useState, useEffect } from "react";
import { Button, Form, Card } from "react-bootstrap";
import axios from "axios";

function Login(props) {
  function handleLogin(e) {
    e.preventDefault();
    let loginData= new FormData(e.target)
    axios
      .post("http://localhost:8080/login", loginData)
      .then((response) => {
        if (response.data.msg === "Successfully logged in!") {
          props.setLoggedIn();
        } else {
          console.log("Login Failed");
        }
      }).catch((error) => { 
        console.log("error", error);
      });
  }
  return (
    <div className="AppLogin mt-5">
      <Card className="mx-auto" style={{ width: "18rem" }}>
        <Card.Header>Login</Card.Header>
        <Card.Body>
          <Form onSubmit={handleLogin}>
            <Form.Group controlId="userid">
              <Form.Label htmlFor="userid">Username</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter Username"
                name="userid"
                required
              />
            </Form.Group>
            <Form.Group className="mb-1" controlId="password">
              <Form.Label htmlFor="password">Password</Form.Label>
              <Form.Control
                type="password"
                placeholder="Enter Password"
                name="password"
                required
              />
              <br></br>
            </Form.Group>

            <Button variant="success" type="submit" value="Submit" >
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
