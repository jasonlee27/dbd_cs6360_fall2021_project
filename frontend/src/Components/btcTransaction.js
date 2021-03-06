import React, { useState } from "react";
import { Button, Form, Card } from "react-bootstrap";
import axios from "axios";
import AssignTrader from "./AssignTrader";

function Transaction(props) {
  let [purchaseType, setPurchaseType] = useState("buy");
  let [bitcoinVal, setBitcoinVal] = useState("");
  let [commissionType, setCommissionType] = useState("");

  function handleTransaction(e) {
    e.preventDefault();
    let transaction = new FormData(e.target);
    if (purchaseType === "buy" || purchaseType === "sell") {
      axios
        .post("http://localhost:8080/profile/buysell", transaction)
        .then((response) => {
          if (response.data.msg === "Successfully purchased.") {
            // e.target.clear();
            console.log(response.data);
          } else {
          }
        })
        .catch((error) => {
          console.log("error", error);
        });
    } else if (purchaseType === "transfer") {
      axios
        .post("http://localhost:8080/profile/transfer", transaction)
        .then((response) => {
          if (response.data.msg === "Successfully purchased.") {
           // e.target.clear();
          } else {
          }
        })
        .catch((error) => {
          console.log("error", error);
        });
    } else if (purchaseType === "add") {
      axios
      .post("http://localhost:8080/profile/add_money", transaction)
      .then((response) => {
        if (response.data.msg === "Successfully added money.") {
       // e.target.clear();
        } else {
        }
      })
      .catch((error) => {
        console.log("error", error);
      });
    }
  
  }
function requestTrader() {
  let transaction = new FormData();
  transaction.append("bitcoin_val", bitcoinVal);
  transaction.append("purchase_type", purchaseType);
  transaction.append("commission_type", commissionType);
  axios
  .post("http://localhost:8080/api/profile/request", transaction)
  .then((response) => {
    if (response.data.msg === "Successfully requested") {
      
    } else {
    }
  })
  .catch((error) => {
    console.log("error", error);
  });
}
  return (
    <div className="BTCTransation m-3">
      <Button onClick={props.logout}>Logout</Button>
      <Card className="mx-auto" style={{ width: "25rem" }}>
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
                value="buy"
                defaultChecked
                onChange={(e) => setPurchaseType("buy")}
              />
              <Form.Check
                inline
                name="purchase_type"
                label="Sell"
                type="radio"
                value="sell"
                onChange={(e) => setPurchaseType("sell")}
              />
              <Form.Check
                inline
                name="purchase_type"
                label="Transfer"
                type="radio"
                value="transfer"
                onChange={(e) => setPurchaseType("transfer")}
              />
              <Form.Check
                inline
                name="purchase_type"
                label="Add Fiat"
                type="radio"
                value="add"
                onChange={(e) => setPurchaseType("add")}
              />
            </Form.Group>
            {(purchaseType === "buy" || purchaseType === "sell") && (
              <div>
                <Form.Group className="mb-3">
                  <Form.Label htmlFor="bitcoin_val">Bitcoin Amount</Form.Label>
                  <Form.Control
                    type="number"
                    placeholder="BTC Amount"
                    name="bitcoin_val"
                    onChange={(e)=>{setBitcoinVal(e.target.value)}}
                  />
                </Form.Group>
          

                <Form.Group className="mb-3">
                  <Form.Label htmlFor="commission_type">
                    Commission Payment
                  </Form.Label>
                  <br></br>
                  <Form.Check
                    inline
                    name="commission_type"
                    label="Bitcoin"
                    type="radio"
                    value="bitcoin"
                    onChange ={(e)=>{setCommissionType("bitcoin")}}
                  />
                  <Form.Check
                    inline
                    name="commission_type"
                    label="Fiat"
                    type="radio"
                    value="fiat"
                    onChange ={(e)=>setCommissionType("fiat")}
                  />
                </Form.Group>
              </div>
            )}
            {purchaseType === "transfer" && (
           
                <Form.Group className="mb-3">
                  <Form.Label htmlFor="usd_val">Fiat Amount</Form.Label>
                  <Form.Control
                    type="number"
                    placeholder="USD Amount"
                    name="usd_val"
                  />
                </Form.Group>
            )}
            {purchaseType === "add" && (
           
           <Form.Group className="mb-3">
             <Form.Label htmlFor="flatcurrency">Fiat Amount</Form.Label>
             <Form.Control
               type="number"
               placeholder="USD Amount"
               name="flatcurrency"
             />
           </Form.Group>
       )}
            <Button variant="success" type="submit">
              Submit
            </Button>
            {(purchaseType === "buy" || purchaseType === "sell" ) && 
            <Button onClick={requestTrader}>
              Request Trader
            </Button>
}
          </Form>
        </Card.Body>
      </Card>
    </div>
  );
}
export default Transaction;
