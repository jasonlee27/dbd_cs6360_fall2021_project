import "./Signup.css";
import React from "react";
import axios from "axios";

function Signup(props) {

  let handleSignup = (e) => {
    e.preventDefault();
    let signupData = new FormData(e.target);
    axios
      .post("http://localhost:5000/register", {
        signupData,
        level: null,
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
        />
        <label htmlFor="password">
          <b>Password</b>
        </label>
        <input
          type="password"
          placeholder="Password"
          name="password"
          required
        />
        <label htmlFor="firstname">
          <b>First Name</b>
        </label>
        <input
          type="text"
          placeholder="First name"
          name="firstname"
          required
        />
        <label htmlFor="lastname">
          <b>Last Name</b>
        </label>
        <input
          type="text"
          placeholder="Last name"
          name="lastname"
          required
        />
        <label htmlFor="phonenumber">
          <b>Phone Number</b>
        </label>
        <input
          type="number"
          placeholder="Phone Number"
          name="phonenumber"
          required
        />
        <label htmlFor="cellphonenumber">
          <b>Cell Phone Number</b>
        </label>
        <input
          type="number"
          placeholder="Cellphone Number"
          name="cellphonenumber"
          required
        />
        <label htmlFor="emailaddress">
          <b>Email Address</b>
        </label>
        <input
          type="email"
          placeholder="Email Address"
          name="emailaddress"
          required
        />
        <label htmlFor="streetaddress1">
          <b>Street Address 1</b>
        </label>
        <input
          type="text"
          placeholder="Street Address1"
          name="streetaddress1"
          required
        />
          <label htmlFor="streetaddress2">
          <b>Street Address 2</b>
        </label>
        <input
          type="text"
          placeholder="Street Address2"
          name="streetaddress2"
          required
        />
        <label htmlFor="city">
          <b>City</b>
        </label>
        <input
          type="text"
          placeholder="City"
          name="city"
          required
        />
        <label htmlFor="state">
          <b>State</b>
        </label>
        <input
          type="text"
          placeholder="State"
          name="state"
          required
        />
        <label htmlFor="zipcode">
          <b>Zip Code</b>
        </label>
        <input
          type="text"
          placeholder="zipcode"
          name="zipcode"
          required
        />
        <input type="submit" value="Submit" />
      </form>
      <button onClick={props.returnToLogin}>
        Return to Login Screen
      </button>
    </div>
  );
}

export default Signup;
