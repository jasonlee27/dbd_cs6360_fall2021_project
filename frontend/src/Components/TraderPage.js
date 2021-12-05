import React, { useEffect } from "react";
import useState from "react-usestateref";
import axios from "axios";
import { Button, Form, Row, Col, Card, Table } from "react-bootstrap";
import Transaction from "./btcTransaction.js";
import ClientSearch from "./ClientSearch.js";

function TraderPage(props) {
  let [purchaseType, setPurchaseType] = useState("buy");
  let [pageStatus, setPageStatus] = useState("transaction");

  function handleTransaction(e) {
    e.preventDefault();
    let transaction = new FormData(e.target);
    if (purchaseType === "buy" || purchaseType === "sell") {
      axios
        .post("http://localhost:8080/profile/buysell", transaction)
        .then((response) => {
          if (response.data.msg === "Successfully purchased.") {
           // e.target.clear();
           console.log(response.data)
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
          e.target.clear();
        } else {
        }
      })
      .catch((error) => {
        console.log("error", error);
      });
    }
  }
  let [
    transactionHistory,
    setTransactionHistory,
    transactionHistoryRef,
  ] = useState("");
  const [isLoading, setIsLoading, isLoadingRef] = useState(false);

  function handleSearch(e) {
    e.preventDefault();
    let searchData = new FormData(e.target);

    axios
      .post("http://localhost:8080/transaction_history", searchData)
      .then((response) => {
        if (response.data.msg === "Successfully clients captured") {
          setTransactionHistory(response.data.clients);
        } else {
        }
      })
      .catch((error) => {
        console.log("error", error);
      });
  }

  useEffect(() => {
    async function fetchData() {
      setIsLoading(true);
      try {
        await handleSearch;
      } catch (error) {
        console.log("error", error);
      }
      setIsLoading(false);
      console.log("trklsijwdj", transactionHistoryRef.current);
    }
    fetchData();
  }, []);

  return (
    <div className="trader m-3">
      <Button onClick={props.logout}>Logout</Button>
      <div className="mt-3">
      <Form.Group className="mb-3">
              <Form.Label htmlFor="page_type">Transaction Type</Form.Label>
              <br></br>
              <Form.Check
                inline
                name="page_type"
                label="Transaction for Client"
                type="radio"
                value="transaction"
                defaultChecked
                onChange={(e) => setPageStatus("transaction")}
              />
              <Form.Check
                inline
                name="page_type"
                label="search"
                type="radio"
                value="search"
                onChange={(e) => setPageStatus("search")}
              />
         
              </Form.Group>
              </div>
      <div class="row">

      {pageStatus === "transaction" && <div class="mx-auto col-sm-1">
      <Card className="mr-1" style={{ width: "18rem" }}>
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
            </Form.Group>
            {(purchaseType === "buy" || purchaseType === "sell") && (
              <div>
                <Form.Group className="mb-3">
                  <Form.Label htmlFor="bitcoin_val">Bitcoin Amount</Form.Label>
                  <Form.Control
                    type="number"
                    placeholder="BTC Amount"
                    name="bitcoin_val"
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
                  />
                  <Form.Check
                    inline
                    name="commission_type"
                    label="Fiat"
                    type="radio"
                    value="fiat"
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
            <Button variant="success" type="submit">
              Submit
            </Button>
          </Form>
        </Card.Body>
      </Card>
      
      </div>
} {pageStatus === "search" &&
      <Card className="ml-1" style={{ width: "20rem" }}>
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
       
            {!isLoading && transactionHistoryRef.current !== "" && (
        <Table striped bordered hover variant="dark">
          <thead>
            <tr>
              <th>Date</th>
              <th>Transactions</th>
            </tr>
          </thead>

          {!isLoading && transactionHistoryRef.current !== "" && (
            <tbody>
              <tr>
                <td>{"hi"}</td>
                {transactionHistoryRef.current.purchase_transaction.map((transaction) => (
                  <td>{transaction}</td>
                ))}
              </tr>
            </tbody>
          )}
        </Table>
      )}
         

            <Button variant="success" type="submit">
              Search
            </Button>
          </Form>
        </Card.Body>
      </Card>
}
    </div>
                
      </div>

  );
}

export default TraderPage;