import "./Signup.css";
import React from "react";
import { Button, Form, Row, Col, Card } from "react-bootstrap";
import useState from "react-usestateref";
import axios from "axios";

function Signup(props) {
  const [username, setUsername] = useState(0);
  const [password, setPassword] = useState(0);
  const [firstName, setFirstName] = useState(0);
  const [lastName, setLastName] = useState(0);
  const [phoneNumber, setPhoneNumber] = useState(0);
  const [cellPhoneNumber, setCellPhoneNumber] = useState(0);
  const [emailAddress, setEmailAddress] = useState(0);
  const [streetAddress1, setStreetAddress1] = useState(0);
  const [streetAddress2, setStreetAddress2] = useState(0);
  const [city, setCity] = useState(0);
  const [state, setState] = useState(0);
  const [zipCode, setZipCode] = useState(0);

  let handleSignup = (e) => {
    e.preventDefault();
    let signupData = new FormData(e.target);
    axios
      .post("http://localhost:5000/register", {
        signupData,
        level: null,
      })
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
                  onChange={(e) => setUsername(e.target.value)}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridPassword">
                <Form.Label>Password</Form.Label>
                <Form.Control
                  required
                  type="password"
                  placeholder="Password"
                  onChange={(e) => setPassword(e.target.value)}
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
                  onChange={(e) => setFirstName(e.target.value)}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formLname">
                <Form.Label>Last Name</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="Doe"
                  onChange={(e) => setLastName(e.target.value)}
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
                  onChange={(e) => setPhoneNumber(e.target.value)}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridCell">
                <Form.Label>Cellphone Number</Form.Label>
                <Form.Control
                  required
                  type="text"
                  placeholder="##########"
                  onChange={(e) => setCellPhoneNumber(e.target.value)}
                />
              </Form.Group>
            </Row>

            <Form.Group className="mb-3" controlId="formGridEmail">
              <Form.Label>Email</Form.Label>
              <Form.Control
                required
                type="email"
                placeholder="Email"
                onChange={(e) => setEmailAddress(e.target.value)}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formGridAddress1">
              <Form.Label>Address</Form.Label>
              <Form.Control
                required
                type="text"
                placeholder="#### Street"
                onChange={(e) => setStreetAddress1(e.target.value)}
              />
            </Form.Group>

            <Form.Group className="mb-3" controlId="formGridAddress2">
              <Form.Label>Address 2</Form.Label>
              <Form.Control
                required
                type="text"
                placeholder="Bldg, Apt, floor, etc"
                onChange={(e) => setStreetAddress2(e.target.value)}
              />
            </Form.Group>

            <Row className="mb-3">
              <Form.Group as={Col} controlId="formGridCity">
                <Form.Label>City</Form.Label>
                <Form.Control
                  required
                  type="text"
                  onChange={(e) => setCity(e.target.value)}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridState">
                <Form.Label>State</Form.Label>
                <Form.Control
                  required
                  type="text"
                  onChange={(e) => setState(e.target.value)}
                />
              </Form.Group>

              <Form.Group as={Col} controlId="formGridZip">
                <Form.Label>Zip</Form.Label>
                <Form.Control
                  required
                  type="text"
                  onChange={(e) => setZipCode(e.target.value)}
                />
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
