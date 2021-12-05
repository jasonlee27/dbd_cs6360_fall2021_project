import React, { useState, useEffect } from "react";
import { Button, Form, Card, Dropdown } from "react-bootstrap";
import axios from "axios";
axios.defaults.withCredentials = true;

function AssignTrader(props) {

    function assignTrader(e) {
        e.preventDefault();
        let traderData= new FormData(e.target);
        axios.post("http://localhost:8080/login", traderData)
        .then((response) => {
          if (response.data.msg === "Successfully logged in!") {
            props.goToTransaction();
          } else {
          }
        }).catch((error) => { 
          console.log("error", error);
        });
    }

    function getAllTraders() {
        axios.get("http://localhost:8080/login")
        .then((response) => {
          if (response.data.msg === "Successfully logged in!") {
            return response.data;
          } else {
          }
        }).catch((error) => { 
          console.log("error", error);
        });
    }
  return (
    <Card className="mx-auto" style={{ width: "18rem" }}>
      <Card.Header>AssignTrader</Card.Header>
      <Card.Body>
        <Dropdown>
          <Dropdown.Toggle variant="success" id="dropdown-basic">
            Dropdown Button
          </Dropdown.Toggle>

          <Dropdown.Menu>
            <Dropdown.Item href="#/action-1">Action</Dropdown.Item>
            <Dropdown.Item href="#/action-2">Another action</Dropdown.Item>
            <Dropdown.Item href="#/action-3">Something else</Dropdown.Item>
          </Dropdown.Menu>
        </Dropdown>
        <Button variant="outline-primary" onClick={assignTrader}>
              Create Account
            </Button>
      </Card.Body>
    </Card>
  );
}

export default AssignTrader;
