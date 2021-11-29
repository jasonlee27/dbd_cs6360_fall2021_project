import "./Signup.css";
import React from "react";
import { Button, Form, Row, Col, Card } from "react-bootstrap";
import useState from "react-usestateref";
import axios from "axios";

function Signup(props) {
  let handleSignup = (e) => {
    e.preventDefault();
    let signupData = new FormData(e.target);
    axios
      .post("http://localhost:8080/register",
        signupData)
      .then((response) => {
        if (response.data.msg === "Logged in successfully !") {
          props.setLoggedIn();
        } else {
          console.log("Login Failed");
        }
      });
  };
  return (
    <div className="Signup mt-5">
      <Card className="mx-auto" style={{ width: "45rem" }}>
        <Card.Header>Signup</Card.Header>
        <Card.Body>
          <Form onSubmit={handleSignup}>
            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridUsername">
                <Form.Label>Username</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="Username"
                  name="username"
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  required
                  type="password"
                  placeholder="Password"
                  name="password"
                />
              </Form.Group>
            </Row>

            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridFname">
                <Form.Label>First Name</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="Jane"
                  name="firstname"
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formLname">
                <Form.Label>Last Name</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="Doe"
                  name="lastname"
                />
              </Form.Group>
            </Row>

            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridPhone">
                <Form.Label>Phone Number</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="##########"
                  name="phonenumber"
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridCell">
                <Form.Label>Cellphone Number</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="##########"
                  name="cellphonenumber"
                />
              </Form.Group>
            </Row>

            <Form.Group className="mb-3" controlId="formGridEmail">
              <Form.Label>Email</Form.Label>
              <Form.Control
                required
                type="email"
                placeholder="Email"
                name="emailaddress"
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formGridAddress1">
              <Form.Label>Address</Form.Label>
              <Form.Control
                required
                type="text"
                placeholder="#### Street"
                name="streetaddress1"
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formGridAddress2">
              <Form.Label>Address 2</Form.Label>
              <Form.Control
                required
                type="text"
                placeholder="Bldg, Apt, floor, etc"
                name="streetaddress2"
              />
            </Form.Group>

            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridCity">
                <Form.Label>City</Form.Label>
                <Form.Control required type="text" name="city" />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridState">
                <Form.Label>State</Form.Label>
                <Form.Control required type="text" name="state" />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridZip">
                <Form.Label>Zip</Form.Label>
                <Form.Control required type="text" name="zipcode" />
              </Form.Group>
            </Row>

            <Button variant="success" type="submit">
              Submit
            </Button>
          </Form>
        </Card.Body>
        <Card.Body>
          <Button
            className=""
            variant="outline-primary"
            onClick={props.returnToLogin}
          >
            Return to Login
          </Button>
        </Card.Body>
      </Card>
    </div>
  );
}

export default Signup;
