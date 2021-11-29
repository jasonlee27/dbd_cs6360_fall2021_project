import React from "react";
import { Button, FormControl, Form } from "react-bootstrap";
import axios from "axios";

function Transaction(props) {

  function handleTransaction(e) {
    e.preventDefault();
    let transaction = new FormData(e.target);
    axios
    .post("http://localhost:8080//api/profile/request", {
        transaction
    })
    .then((response) => {
      if (response.data.msg === "Successfully logged in!") {
        props.setLoggedIn();
      } else {
      
      }
    });
  }

  return (
    <div className="App">
      <header className="Transaction"></header>
      <Form className="m-3" onSubmit={handleTransaction}>
        <Form.Group className="mb-3" controlId="formBuySell">
          <Form.Label>Transaction Type</Form.Label>
          <Form.Check inline name="purchase_type" label="Buy" type="radio" value="Buy"/>
          <Form.Check inline name="purchase_type"label="Sell" type="radio" value="Sell"/>
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBtcAmount">
          <Form.Label>Bitcoin Amount</Form.Label>
          <Form.Control type="text" placeholder="BTC Amount"  name="bitcoin_val" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBuySell">
          <Form.Label>Commission Payment</Form.Label>
          <Form.Check inline name="commission_type" label="Bitcoin" type="radio" value="Bitcoin"/>
          <Form.Check inline name="commission_type" label="Fiat" type="radio" value="Fiat"/>
        </Form.Group>

        <Button variant="success" type="submit">
          Submit
        </Button>
      </Form>
    </div>
  );
}
export default Transaction;
