import React, { useState } from "react";
import { Button, Form, Card } from "react-bootstrap";
import axios from "axios";

function Transaction(props) {
  function handleTransaction(e) {
    e.preventDefault();
    let transaction = new FormData(e.target);
    axios
      .post("http://localhost:8080/profile/buysell", transaction)
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
    <div className="BTCTransation mt-5">
      <Button onClick={props.logout}>
        Logout
      </Button>
      <Card className="mx-auto" style={{ width: "18rem" }}>
        <Card.Header>Bitcoin Transaction</Card.Header>
        <Card.Body>
          <Form onSubmit={handleTransaction}>
            <Form.Group className="mb-3">
              <Form.Label htmlFor="purchase_type">Transaction Type</Form.Label>
              <br></br>
              <Form.Check
                inline
                name="purchase_type"
                label="Buy"
                type="radio"
                value="Buy"
              />
              <Form.Check
                inline
                name="purchase_type"
                label="Sell"
                type="radio"
                value="Sell"
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label htmlFor="bitcoin_val">Bitcoin Amount</Form.Label>
              <Form.Control
                type="text"
                placeholder="BTC Amount"
                name="bitcoin_val"
              />
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label htmlFor="commission_type">Commission Payment</Form.Label>
              <br></br>
              <Form.Check
                inline
                name="commission_type"
                label="Bitcoin"
                type="radio"
                value="Bitcoin"
              />
              <Form.Check
                inline
                name="commission_type"
                label="Fiat"
                type="radio"
                value="Fiat"
              />
            </Form.Group>

            <Button variant="success" type="submit">
              Submit
            </Button>
          </Form>
        </Card.Body>
      </Card>
    </div>
  );
}
export default Transaction;
