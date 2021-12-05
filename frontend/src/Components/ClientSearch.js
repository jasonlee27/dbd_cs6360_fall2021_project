import React from "react";
import useState from "react-usestateref";
import axios from "axios";
import { Button, Form, Row, Col, Card } from "react-bootstrap";

function ClientSearch(props) {
  function handleSearch(e) {
    e.preventDefault();
    let searchData = new FormData(e.target);

    axios
      .post("http://localhost:8080/profile/buysell", searchData)
      .then((response) => {
        if (response.data.msg === "Successfully purchased.") {
          e.target.clear();
        } else {
        }
      })
      .catch((error) => {
        console.log("error", error);
      });
  }

  return (
    <div className="Client-Search mt-5">
      <Button onClick={props.logout}>Logout</Button>
      <Card className="mx-auto" style={{ width: "30rem" }}>
        <Card.Header>Client Search</Card.Header>
        <Card.Body>
          <Form onSubmit={handleSearch}>
            <Row className="mb-3">
            
              <Form.Group as={Col}>
              <Form.Label htmlFor="userid">Client ID</Form.Label>
                <Form.Control
                  required
                  type="text"
                  name="userid"
                  PlaceHolder="Client ID"
                />
              </Form.Group>
            </Row>
            <Row className="mb-3">
              <Form.Group as={Col}>
              <Form.Label htmlFor="firstname">First Name</Form.Label>
                <Form.Control
                  required
                  type="text"
                  name="firstname"
                  PlaceHolder="First Name"
                />
              </Form.Group>
            </Row>
            <Row className="mb-3">
              <Form.Group as={Col}>
              <Form.Label htmlFor="lastname">Last Name</Form.Label>
                <Form.Control
                  type="text"
                  name="lastname"
                  PlaceHolder="Last Name"
                />
              </Form.Group>
            </Row>
            <Row className="mb-3">
              <Form.Group as={Col}>
              <Form.Label htmlFor="address1">Address </Form.Label>
                <Form.Control
                  type="text"
                  name="address1"
                  PlaceHolder="Address"
                />
              </Form.Group>
            </Row>
            <Row className="mb-3">
              <Form.Group as={Col}>
              <Form.Label htmlFor="address2">Address 2</Form.Label>
                <Form.Control
                  type="text"
                  name="address2"
                  PlaceHolder="Address 2"
                />
              </Form.Group>
            </Row>
            <Row className="mb-3">
              <Form.Group as={Col}>
              <Form.Label htmlFor="city">City</Form.Label>
                <Form.Control
                  required
                  type="text"
                  name="city"
                />
              </Form.Group>

              <Form.Group as={Col}>
                <Form.Label htmlFor="state">State</Form.Label>
                <Form.Control required type="text" name="state" />
              </Form.Group>

              <Form.Group as={Col} >
                <Form.Label htmlFor="zipcode">Zip</Form.Label>
                <Form.Control required type="text" name="zipcode" />
              </Form.Group>
  
            </Row>

            <Button variant="success" type="submit">
              Search
            </Button>
          </Form>
        </Card.Body>
      </Card>
    </div>
  );
}

export default ClientSearch;
