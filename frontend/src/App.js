import logo from "./logo.svg";
import "./App.css";
import Request from "axios-react";
import React, { useState, useEffect } from 'react'

function App() {
  const [username, setUsername] = useState(0);
  const [password, setPassword] = useState(0);
  function handleLogin(e, username, password) {
    <div>
      <Request
        config={{
          method: "get",
          url: `http://localhost:8080/${username}`,
        }}
      >
        {({ loading, response, error, refetch, networkStatus }) => (
      
          <div>
            {networkStatus && <span>{networkStatus}</span>}
            {loading && <span>Loading...</span>}
            {error && <span>{error.response.data}</span>}
            {response && <h3>{response.data.title}</h3>}
            <button onClick={refetch}>Refetch!</button>
          </div>
        )}
      </Request>

      <Request
        config={{
          method: "get",
          url: `http://localhost:8080/${password}`,
        }}
      >
        {({ loading, response, error, refetch, networkStatus }) => (
          <div>
            {networkStatus && <span>{networkStatus}</span>}
            {loading && <span>Loading...</span>}
            {error && <span>{error.response.data}</span>}
            {response && <h3>{response.data.title}</h3>}
            <button onClick={refetch}>Refetch!</button>
          </div>
        )}
      </Request>
    </div>;
  }

  return (
    <div className="App">
      <header className="Login"></header>
      <form>
        <label for="username">
          <b>Username</b>
        </label>
        <input
          type="text"
          placeholder="Enter Username"
          name="username"
          required
          onChange={(e)=>setUsername(e.target.value)}
        />
        <label for="password">
          <b>Password</b>
        </label>
        <input
          type="password"
          placeholder="Enter Password"
          name="password"
          required
          onChange={(e)=>setPassword(e.target.value)}
        />
        <button type="submit" onClick={handleLogin}>
          login
        </button>
      </form>
      <div>
        Don't have an account? <a href="www.google.com">Click Here</a>
      </div>
    </div>
  );
}

export default App;
