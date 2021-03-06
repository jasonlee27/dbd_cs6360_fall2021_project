//Gabriel Goldstein gjg180000
//megan tran mjt170002
//jaeseonglee, jxl115330
//Yibp Li
import React, { useEffect } from "react";
import useState from "react-usestateref";
import axios from "axios";
import moment from "moment";
import { Button, Form, Row, Col, Card, Table } from "react-bootstrap";
import Picker from "react-month-picker";

function ManagerSearch(props) {
  let [dateRange, setDateRange, dateRangeRef] = useState("Daily");
  let [
    transactionHistory,
    setTransactionHistory,
    transactionHistoryRef,
  ] = useState("");
  const [isLoading, setIsLoading, isLoadingRef] = useState(false);
  async function handleSearch(e) {
    e.preventDefault();
    let searchData = new FormData(e.target);

    await axios
      .post("http://localhost:8080/profile/manager/history", searchData)
      .then((response) => {
        console.log("data:", response.data);
        if (
          response.data.msg === "Successfully received transaction history."
        ) {
          setTransactionHistory(response.data.history);
          console.log("transaction history:", transactionHistoryRef.current);
        } else {
          console.log("else");
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
    <div className="Manager-Search m-3">
      <Button onClick={props.logout}>Logout</Button>
      <Card className="mx-auto" style={{ width: "20rem" }}>
        <Card.Header>Transactions Search</Card.Header>
        <Card.Body>
          <Form onSubmit={handleSearch}>
            <Row className="mb-3">
              <Form.Group className="mb-3">
                <Form.Label htmlFor="daterange">Date Range</Form.Label>
                <br></br>
                <Form.Check
                  inline
                  name="daterange"
                  label="Daily"
                  type="radio"
                  value="Daily"
                  defaultChecked
                  onChange={(e) => setDateRange("Daily")}
                />
                <Form.Check
                  inline
                  name="daterange"
                  label="Weekly"
                  type="radio"
                  value="Weekly"
                  onChange={(e) => setDateRange("Weekly")}
                />
                <Form.Check
                  inline
                  name="daterange"
                  label="Monthly"
                  type="radio"
                  value="Monthly"
                  onChange={(e) => setDateRange("Monthly")}
                />
              </Form.Group>
            </Row>
            <Row className="mb-3">
              <Form.Group as={Col}>
                <Form.Label htmlFor="startdate">Start Date</Form.Label>
                <Form.Control
                  required
                  type="date"
                  name="startdate"
                  max={moment().format("YYYY-MM-DD")}
                  showClearButton
                />
              </Form.Group>

              <Form.Group as={Col}>
                <Form.Label htmlFor="enddate">End Date</Form.Label>
                <Form.Control
                  required
                  type="date"
                  name="enddate"
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

      {!isLoading && transactionHistoryRef.current !== "" && (
        <Table striped bordered hover variant="dark">
          <thead>
            <tr>
              <th>Date</th>
              <th>Time</th>
              <th>Commission Type</th>
              <th>Commission Rate</th>
              <th>Bitcoin Value</th>
              <th>Fiat Value</th>
              <th>Purchase Type</th>
            </tr>
          </thead>

          {!isLoading && transactionHistoryRef.current !== "" && (
            <tbody>
              {transactionHistoryRef.current.purchase_transaction.map(
                (transaction) => (
                  <tr>
                    <td>{transaction.date}</td>
                    <td>{transaction.time}</td>
                    <td>{transaction.commission_type}</td>
                    <td>{transaction.commission_rate}</td>
                    <td>{transaction.bitcoin_value}</td>
                    <td>{transaction.fiat_value}</td>
                    <td>{transaction.purchase_type}</td>
                  </tr>
                )
              )}
            </tbody>
          )}
        </Table>
      )}
    </div>
  );
}

export default ManagerSearch;
