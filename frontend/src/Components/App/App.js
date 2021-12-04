import "./App.css";
import Login from "../Login/Login.js";
import Signup from "../Signup/Signup.js";
import Transaction from "../btcTransaction.js";
import React from 'react';
import useState from 'react-usestateref';
import {BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
  useNavigate,
} from "react-router-dom";

function App() {
  const [state, setState] = useState('login');
  let navigate = useNavigate();

  let handleCreateNewAccount = () => {
    setState('signup');
  navigate('/signup')
  };
  let handleReturnToLogin  = () => {
    setState('login');
    navigate('/login')
  };
  let handleLogin  = () => {
    setState('loggedIn');
    navigate('/transaction')
  };
  let handleLogout  = () => {
    setState('login');
    navigate('/login')
  };
  return (
    <Routes>
      <Route
        path="/"
        element={<Login createNewAccount={handleCreateNewAccount} setLoggedIn={handleLogin}/>}
      />
      <Route
        path="/login"
        element={<Login createNewAccount={handleCreateNewAccount} setLoggedIn={handleLogin}/>}
      />
        <Route
        path="/signup"
        element={<Signup returnToLogin={handleReturnToLogin} setLoggedIn={handleLogin}/>}
      />
        <Route 
        path="/transaction"
        element={state==='loggedIn' ? <Transaction logout={handleLogout} /> :  <Navigate to="/login" />}
    />
    </Routes>
);
/*
    <div>
     {state==='login' && 
        <Login createNewAccount={handleCreateNewAccount} setLoggedIn={handleLogin}/>
      }
      {state==='signup' && 
        <Signup returnToLogin={handleReturnToLogin} setLoggedIn={handleLogin} />}
      {state==='btcTransaction' && 
        <Transaction />}
    </div>
    
  )
  */
}


export default App;
