import "./Signup.css";
import React from "react";
import useState from 'react-usestateref';
import axios from "axios";

function Signup(props) {
  const [username, setUsername] = useState(0);
  const [password, setPassword] = useState(0);
  const [firstName, setFirstName] = useState(0);
  const [lastName, setLastName] = useState(0);
  const [phoneNumber, setPhoneNumber] = useState(0);
  const [cellPhoneNumber, setCellPhoneNumber] = useState(0);
  const [emailAddress, setEmailAddress] = useState(0);
  const [streetAddress1, setStreetAddress1] = useState(0);
  const [streetAddress2, setStreetAddress2] = useState(0);
  const [city, setCity] = useState(0);
  const [state, setState] = useState(0);
  const [zipCode, setZipCode] = useState(0);

  let handleSignup = () => {
    axios
      .post("http://localhost:5000/register", {
        username: username,
        password: password,
        clientid: null,
        client_password: null,
        firstname: firstName,
        lastname: lastName,
        email: emailAddress,
        address1: streetAddress1,
        address2: streetAddress2,
        city: city,
        state: state,
        zipcode: zipCode,
        cellphone: cellPhoneNumber,
        phone: phoneNumber,
        level: null,
        bitcoin: null,
        flatcurrency: null,
      })
      .then((response) => { 
        if(response.data.msg === 'Logged in successfully !') {
            props.setLoggedIn();
        }
        else {
          console.log('Login Failed');
        }
      });
  };
  return (
    <div className="Signup">
      <form onSubmit={handleSignup}>
        <label htmlFor="username">
          <b>Username</b>
        </label>
        <input
          type="text"
          placeholder="Username"
          name="username"
          required
          onChange={(e) => setUsername(e.target.value)}
        />
        <label htmlFor="password">
          <b>Password</b>
        </label>
        <input
          type="password"
          placeholder="Password"
          name="password"
          required
          onChange={(e) => setPassword(e.target.value)}
        />
        <label htmlFor="firstname">
          <b>First Name</b>
        </label>
        <input
          type="text"
          placeholder="First name"
          name="firstname"
          required
          onChange={(e) => setFirstName(e.target.value)}
        />
        <label htmlFor="lastname">
          <b>First Name</b>
        </label>
        <input
          type="text"
          placeholder="Last name"
          name="lastname"
          required
          onChange={(e) => setLastName(e.target.value)}
        />
        <label htmlFor="phonenumber">
          <b>Phone Number</b>
        </label>
        <input
          type="number"
          placeholder="Phone Number"
          name="phonenumber"
          required
          onChange={(e) => setPhoneNumber(e.target.value)}
        />
        <label htmlFor="cellphonenumber">
          <b>Cell Phone Number</b>
        </label>
        <input
          type="number"
          placeholder="Cellphone Number"
          name="cellphonenumber"
          required
          onChange={(e) => setCellPhoneNumber(e.target.value)}
        />
        <label htmlFor="emailaddress">
          <b>Cell Phone Number</b>
        </label>
        <input
          type="email"
          placeholder="Email Address"
          name="emailaddress"
          required
          onChange={(e) => setEmailAddress(e.target.value)}
        />
        <label htmlFor="streetaddress1">
          <b>Cell Phone Number</b>
        </label>
        <input
          type="text"
          placeholder="Street Address1"
          name="streetaddress1"
          required
          onChange={(e) => setStreetAddress1(e.target.value)}
        />
          <label htmlFor="streetaddress2">
          <b>Cell Phone Number</b>
        </label>
        <input
          type="text"
          placeholder="Street Address2"
          name="streetaddress2"
          required
          onChange={(e) => setStreetAddress2(e.target.value)}
        />
        <label htmlFor="city">
          <b>Cell Phone Number</b>
        </label>
        <input
          type="text"
          placeholder="City"
          name="city"
          required
          onChange={(e) => setCity(e.target.value)}
        />
        <label htmlFor="state">
          <b>State</b>
        </label>
        <input
          type="text"
          placeholder="State"
          name="state"
          required
          onChange={(e) => setState(e.target.value)}
        />
        <label htmlFor="zipcode">
          <b>Zip Code</b>
        </label>
        <input
          type="text"
          placeholder="zipcode"
          name="zipcode"
          required
          onChange={(e) => setZipCode(e.target.value)}
        />
        <input type="submit" value="Submit" />
      </form>
    </div>
  );
}

export default Signup;
