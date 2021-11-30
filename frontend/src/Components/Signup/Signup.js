import "./Signup.css";
import React from "react";
import { Button, Form, Row, Col, Card } from "react-bootstrap";
import useState from "react-usestateref";
import axios from "axios";

function Signup(props) {
  let handleSignup = (e) => {
    e.preventDefault();
    var signupFormData = new FormData();
    signupFormData.append("userid", formData.userid)
    signupFormData.append("password", formData.password)
    signupFormData.append("usertype", formData.usertype)
    signupFormData.append("firstname", formData.firstname)
    signupFormData.append("lastname", formData.lastname)
    signupFormData.append("address1", formData.address1)
    signupFormData.append("address2", formData.address2)  
    signupFormData.append("city", formData.city)
    signupFormData.append("zipcode", formData.zipcode)
    signupFormData.append("state", formData.state)
    signupFormData.append("cphone", formData.cellphonenumber)
    signupFormData.append("phone", formData.phonenumber)
    signupFormData.append("email", formData.email)
      
    axios
      .post("http://localhost:8080/register", signupFormData)
      .then((response) => {
        if (response.data.msg === "Successfully registered") {
          props.setLoggedIn();
        } else {
          console.log("Signup Failed");
        }
      });
  };

  const initialFormData = Object.freeze({
      username: "",
      password: "",
      usertype: "client",
      firstname: "",
      lastname: "",
      address1: "",
      address2: "",
      city: "",
      zipcode: "",
      state: "",
      cellphonenumber: "",
      phonenumber: "",
      email: "",
  });
  const [formData, updateFormData] = React.useState(initialFormData);
  const handleChange = (e) => {
    updateFormData({
      ...formData,

      // Trimming any whitespace
      [e.target.name]: e.target.value.trim()
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
                  onChange={handleChange}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  required
                  type="password"
                  placeholder="Password"
                  name="password"
                  onChange={handleChange}
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
                  onChange={handleChange}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formLname">
                <Form.Label>Last Name</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="Doe"
                  name="lastname"
                  onChange={handleChange}
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
                  onChange={handleChange}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridCell">
                <Form.Label>Cellphone Number</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="##########"
                  name="cellphonenumber"
                  onChange={handleChange}
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
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formGridAddress1">
              <Form.Label>Address 1</Form.Label>
              <Form.Control
                required
                type="text"
                placeholder="#### Street"
                name="address1"
                onChange={handleChange}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formGridAddress2">
              <Form.Label>Address 2</Form.Label>
              <Form.Control
                required
                type="text"
                placeholder="Bldg, Apt, floor, etc"
                name="address2"
                onChange={handleChange}
              />
            </Form.Group>

            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridCity">
                <Form.Label>City</Form.Label>
                <Form.Control
                  required
                  type="text"
                  name="city"
                  onChange={handleChange}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridState">
                <Form.Label>State</Form.Label>
                <Form.Control required type="text" name="state" onChange={handleChange}/>
              </Form.Group>

              <Form.Group as={Col} controlId="formGridZip">
                <Form.Label>Zip</Form.Label>
                <Form.Control required type="text" name="zipcode" onChange={handleChange}/>
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
