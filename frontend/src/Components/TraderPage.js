import React from "react";
import useState from "react-usestateref";
import axios from "axios";
import { Button, Form, Row, Col, Card } from "react-bootstrap";
import Transaction from "./btcTransaction.js";
import ClientSearch from "./ClientSearch.js";

function TraderPage(props) {
  return (
    <div>
      <ClientSearch></ClientSearch>
      <Transaction></Transaction>
    </div>
  );
}

export default TraderPage;