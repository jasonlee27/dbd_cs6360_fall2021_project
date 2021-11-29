import React, { useState } from "react";
import { Button, FormControl, Form } from "react-bootstrap";
import axios from "axios";

function Transaction(props) {
  const [username, setUsername] = useState(0);
  const [password, setPassword] = useState(0);

  function handleTransaction(e, username, password) {
    //todo
  }

  return (
    <div className="App">
      <header className="Transaction"></header>
      <Form className="m-3" onSubmit={handleLogin}>
        <Form.Group className="mb-3" controlId="formBuySell">
          <Form.Label>Transaction Type</Form.Label>
          <Form.Check inline label="Buy" type="radio" />
          <Form.Check inline label="Sell" type="radio" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBtcAmount">
          <Form.Label>Bitcoin Amount</Form.Label>
          <Form.Control type="text" placeholder="BTC Amount" />
        </Form.Group>

        <Form.Group className="mb-3" controlId="formBuySell">
          <Form.Label>Commission Payment</Form.Label>
          <Form.Check inline label="Bitcoin" type="radio" />
          <Form.Check inline label="Fiat" type="radio" />
        </Form.Group>

        <Button variant="success" type="submit">
          Submit
        </Button>
      </Form>
    </div>
  );
}
export default Login;
