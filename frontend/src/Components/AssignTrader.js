//Gabriel Goldstein gjg180000
//megan tran mjt170002
//jaeseonglee, jxl115330
//Yibp Li
import React, {useEffect} from "react";
import { Button, Form, Card, Dropdown, DropdownButton } from "react-bootstrap";
import axios from "axios";
import useState from "react-usestateref";
axios.defaults.withCredentials = true;


function AssignTrader(props) {

    
const [ isLoading, setIsLoading] = useState(false);
  let [traders, setTraders, tradersRef] = useState("");
  let [selectedTrader, setSelectedTrader, selectedTraderRef] = useState("");

  function assignTrader(e) {
    //e.preventDefault();
   let traderData = new FormData();
   traderData.append("traderid",selectedTraderRef.current);
    console.log("selected data: ", selectedTraderRef.current);
    axios
      .post("http://localhost:8080/profile/assign", traderData)
      .then((response) => {
        if (response.data.msg === "Successfully assigned trader") {
            console.log("YAY");
          props.goToTransaction();
        } else {
        }
      })
      .catch((error) => {
        console.log("error", error);
      });
  }

  async function getAllTraders() {
    await axios
      .post("http://localhost:8080/profile/traders")
      .then((response) => {
        if (response.data.msg === "Successfully found all traders") {
          console.log("t1:", response.data.traders);
          setTraders(response.data.traders);
        } else {
          //console.log("t2:",response.data.traders);
          //   return response.data.traders
        }
      })
      .catch((error) => {
        console.log("error", error);
      });
  }
  useEffect( () => { 
    async function fetchData() {
        setIsLoading(true);
        try {
            await getAllTraders();
        } catch (error) {
            console.log("error", error);
        }
        setIsLoading(false);
        console.log("trklsijwdj", tradersRef.current);
    }
    fetchData();
}, []);

function handleSelect(e) {
    console.log("you selected: ", e);
    setSelectedTrader(e);

}
  return (
    <div className="Assign-Trader mt-5">
      <Card className="mx-auto" style={{ width: "18rem" }}>
        <Button onClick={props.logout}>Logout</Button>
        <Card.Header>AssignTrader</Card.Header>
        <Card.Body>
            <Form onSubmit={assignTrader}>
          <Dropdown>

            <DropdownButton
      title="Choose Trader"
      id="dropdown-menu-align-right"
      onSelect={handleSelect}>
              {
                !isLoading &&tradersRef.current !== "" &&
                tradersRef.current.map((trader, index) => (
                    <Dropdown.Item eventKey ={trader.traderid} value={ trader.traderid }>
                      { trader.firstname } { trader.lastname }
                    </Dropdown.Item>
                )
            )}
            </DropdownButton>
          </Dropdown>
          <Button variant="outline-primary" onClick={assignTrader}>
            Submit
          </Button>
          </Form>
        </Card.Body>
      </Card>
    </div>
  );
}

export default AssignTrader;
