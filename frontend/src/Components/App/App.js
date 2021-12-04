import "./App.css";
import Login from "../Login/Login.js";
import Signup from "../Signup/Signup.js";
import Transaction from "../btcTransaction.js";
import ManagerSearch from "../ManagerSearch.js";
import React from 'react';
import useState from 'react-usestateref';
import axios from "axios";
import {BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
  useNavigate,
} from "react-router-dom";

function App() {
  const [state, setState] = useState('login');
  const [userType, setUserType] = useState('');
  let navigate = useNavigate();

  function getUserInfo(userId) {
    console.log("userid",userId);
    let formData = new FormData();
    formData.append("userid", userId);
    axios
    .post("http://localhost:8080/api/profile/userInfo", formData)
    .then((response) => {
      if(response.data.account_info !== ""){
        console.log(response.data.account_info.user_type);
        setUserType(response.data.account_info.user_type);
      }
    }).catch((error) => { 
      console.log("error", error);
    });
  }

  function handleLogoutEvent(e) {
    axios
      .request("http://localhost:8080/logout")
      .then((response) => {
        if (response.data.msg === "Successfully logged out") {
            handleLogout();
        }
      }).catch((error) => {
        console.log("error", error);
      });
  }

  let handleCreateNewAccount = () => {
    setState('signup');
  navigate('/signup')
  };
  let handleReturnToLogin  = () => {
    setState('login');
    navigate('/login')
  };
  let handleLogin  = (userId) => {
    setState('loggedIn');
    getUserInfo(userId);
    console.log("1111:",userType);
    if(userType==="client" ||userType==="trader"){
    navigate('/transaction')
    }
    else if(userType==="manager") {
      navigate('/transactions/search')
    }
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
        element={state==='loggedIn' && userType === 'client' ? <Transaction logout={handleLogoutEvent} /> :  <Navigate to="/login" />}
    />
   <Route 
        path="/transaction"
        element={state==='loggedIn' && userType === 'trader' ? <Transaction logout={handleLogoutEvent} /> :  <Navigate to="/login" />}
/>
        <Route 
        path="/transactions/search"
        element={state==='loggedIn' && userType === 'manager' ? <ManagerSearch logout={handleLogoutEvent} /> :  <Navigate to="/login" />}
        />

    </Routes>
);
}


export default App;
