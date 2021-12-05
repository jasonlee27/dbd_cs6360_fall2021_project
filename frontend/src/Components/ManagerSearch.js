import React from "react";
import useState from "react-usestateref";
import axios from "axios";
import moment from 'moment';
import { Button, Form, Row, Col, Card } from "react-bootstrap";
import Picker from 'react-month-picker';

function ManagerSearch(props) {

    let [dateRange, setDateRange] = useState("Daily");
    let [transactionHistory, setTransactionHistory] = useState(null);
  function handleSearch(e) {
    let searchData = new FormData(e.target);

    axios
      .post("http://localhost:8080/profile/manager/history", searchData)
      .then((response) => {
        if (response.data.msg === "Successfully received transaction history.") {
            transactionHistory(response.data.transaction_history);
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
              <Form.Label htmlFor="time_period">Date Range</Form.Label>
              <br></br>
              <Form.Check
                inline
                name="time_period"
                label="Daily"
                type="radio"
                value="Daily"
                defaultChecked
                onChange={(e)=> setDateRange("Daily")}
              />
              <Form.Check
                inline
                name="time_period"
                label="Weekly"
                type="radio"
                value="Weekly"
                onChange={(e)=> setDateRange("Weekly")}
              />
                <Form.Check
                inline
                name="time_period"
                label="Monthly"
                type="radio"
                value="Monthly"
                onChange={(e)=> setDateRange("Monthly")}
              />
            </Form.Group>
            </Row>
          <Row className="mb-3">

          <Form.Label htmlFor="start_date">Start Date</Form.Label>
            <Form.Group as={Col}>
              <Form.Control
                required
                type="date"
                name="start_date"
                max={moment().format("YYYY-MM-DD")}
                showClearButton
              />
            </Form.Group>
            <Form.Label htmlFor="end_date">End Date</Form.Label>
            <Form.Group as={Col}>
              <Form.Control
                required
                type="date"
                name="end_date"
                max={moment().format("YYYY-MM-DD")}
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
