import React, { useEffect } from "react";
import useState from "react-usestateref";
import axios from "axios";
import { Button, Form, Row, Col, Card, Table } from "react-bootstrap";

function ClientSearch(props) {

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
      .post("http://localhost:8080/clients_assigned", searchData)
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
    </div>
  );
}

export default ClientSearch;
