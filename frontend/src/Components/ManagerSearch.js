import React from "react";
import useState from "react-usestateref";
import axios from "axios";
import moment from 'moment';
import { Button, Form, Row, Col, Card } from "react-bootstrap";
import Picker from 'react-month-picker';

function ManagerSearch(props) {

    let [dateRange, setDateRange] = useState("Daily");
  function handleSearch(e) {
    let searchData = new FormData(e.target);

    axios
      .post("http://localhost:8080/profile/buysell", searchData)
      .then((response) => {
        if (response.data.msg === "Successfully purchased.") {
          e.target.clear();
        } else {
        }
      }).catch((error) => {
        console.log("error", error);
      });

  }

  return (
    <div className="Manager-Search mt-5">
         <Button onClick={props.logout}>
        Logout
      </Button>
    <Card className="mx-auto" style={{ width: "20rem" }}>
      <Card.Header>Transactions Search</Card.Header>
      <Card.Body>
        <Form onSubmit={handleSearch}>
        <Row className="mb-3">
        <Form.Group className="mb-3" controlId="dateRange">
              <Form.Label htmlFor="dateRange">Date Range</Form.Label>
              <br></br>
              <Form.Check
                inline
                name="dateRange"
                label="Daily"
                type="radio"
                value="Daily"
                defaultChecked
                onChange={(e)=> setDateRange("Daily")}
              />
              <Form.Check
                inline
                name="dateRange"
                label="Weekly"
                type="radio"
                value="Weekly"
                onChange={(e)=> setDateRange("Weekly")}
              />
                <Form.Check
                inline
                name="dateRange"
                label="Monthly"
                type="radio"
                value="Monthly"
                onChange={(e)=> setDateRange("Monthly")}
              />
            </Form.Group>
            </Row>
          <Row className="mb-3">

          <Form.Label htmlFor="startDate">Start Date</Form.Label>
            <Form.Group as={Col}>
              <Form.Control
                required
                type="date"
                name="startDate"
                maxDate={moment().format("YYYY-MM-DD")}
                showClearButton
              />
            </Form.Group>
            <Form.Label htmlFor="endDate">End Date</Form.Label>
            <Form.Group as={Col}>
              <Form.Control
                required
                type="date"
                name="endDate"
                maxDate={moment().format("YYYY-MM-DD")}
                showClearButton
              />
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

export default ManagerSearch;
