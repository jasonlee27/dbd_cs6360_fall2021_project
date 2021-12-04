import "./Signup.css";
import React from "react";
import { Button, Form, Row, Col, Card } from "react-bootstrap";
import useState from "react-usestateref";
import axios from "axios";

function Signup(props) {

  let [clientChecked,setClientChecked]= useState(true);

  let handleSignup = (e) => {
    e.preventDefault();
    let signupData = new FormData(e.target);
    console.log("userid", signupData.get("userid"));
    axios
      .post("http://localhost:8080/register", signupData)
      .then((response) => {
        if (response.data.msg === "Successfully registered") {
          props.setLoggedIn(signupData.get("userid"));
        } else {
          console.log("Signup Failed");
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
          <Form.Group controlId="user-type">
              <Form.Label htmlFor="usertype">User Type</Form.Label>
              <br></br>
              <Form.Check
                inline
                name="usertype"
                label="Client"
                type="radio"
                value="client"
                onChange={((e) => setClientChecked(true))}
                defaultChecked
              />
              <Form.Check
                inline
                name="usertype"
                label="Trader"
                id="2"
                type="radio"
                value="trader"
                onChange={((e) => setClientChecked(false))}
              />
               <Form.Check
                inline
                name="usertype"
                label="Manager"
                id="3"
                type="radio"
                value="manager"
                onChange={((e) => setClientChecked(false))}
              />
      
            </Form.Group>
            </Row>
            <Row className="mb-3">
              <Form.Group as={Col} controlId="userid">
                <Form.Label htmlFor="userid">Username</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="Username"
                  name="userid"
                />
              </Form.Group>

              <Form.Group as={Col} controlId="password">
                <Form.Label htmlFor="password">Password</Form.Label>
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
                <Form.Label htmlFor="firstname">First Name</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="Jane"
                  name="firstname"
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formLname">
                <Form.Label htmlFor="lastname">Last Name</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="Doe"
                  name="lastname"
                />
              </Form.Group>
            </Row>
            {clientChecked && 
              (
          <div>
            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridPhone">
                <Form.Label htmlFor="phonenumber">Phone Number</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="##########"
                  name="phonenumber"
                  maxLength={10}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridCell">
                <Form.Label htmlFor="cellphonenumber">Cellphone Number</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="##########"
                  name="cellphonenumber"
                  maxLength={10}
                />
              </Form.Group>
            </Row>

            <Form.Group className="mb-3" controlId="formGridEmail">
              <Form.Label htmlFor="emailaddress">Email</Form.Label>
              <Form.Control
                required
                type="email"
                placeholder="Email"
                name="emailaddress"
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formGridAddress1">
              <Form.Label htmlFor="address1">Address 1</Form.Label>
              <Form.Control
                required
                type="text"
                placeholder="#### Street"
                name="address1"
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formGridAddress2">
              <Form.Label htmlFor="address2">Address 2</Form.Label>
              <Form.Control
                required
                type="text"
                placeholder="Bldg, Apt, floor, etc"
                name="address2"
              />
            </Form.Group>

            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridCity">
                <Form.Label htmlFor="city">City</Form.Label>
                <Form.Control
                  required
                  type="text"
                  name="city"
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridState">
                <Form.Label htmlFor="state">State</Form.Label>
                <Form.Control required type="text" name="state" />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridZip">
                <Form.Label htmlFor="zipcode">Zip</Form.Label>
                <Form.Control required type="text" name="zipcode" />
              </Form.Group>
  
            </Row>
            </div>
              )}

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
