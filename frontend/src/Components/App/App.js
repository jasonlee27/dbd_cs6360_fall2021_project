import "./App.css";
import Login from "../Login/Login.js";
import Signup from "../Signup/Signup.js";
import Transaction from "../btcTransaction.js";
import ManagerSearch from "../ManagerSearch.js";
import TraderPage from "../TraderPage.js";
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
  const [userType, setUserType, userTypeRef] = useState('');
  let navigate = useNavigate();

  async function getUserInfo(userId) {
    console.log("userid",userId);
    let formData = new FormData();
    formData.append("userid", userId);
    await axios
    .post("http://localhost:8080/api/profile/userInfo", formData)
    .then((response) => {
      if(response.data.account_info !== ""){
        console.log(response.data.account_info.user_type);
        setUserType(response.data.account_info.user_type);
        return Promise.resolve(1);
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
  let handleLogin  = async (userId) => {
    setState('loggedIn');
   getUserInfo(userId).then((response)=> {
    console.log(userTypeRef.current);
    if(userTypeRef.current==="client"){
    navigate('/transaction')
    }
    else if(userTypeRef.current==="trader") {
      navigate('/trader')
    }
    else if(userTypeRef.current==="manager") {
      navigate('/transactions/search')
    }
  });
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
        path="/trader"
        element={state==='loggedIn' && userType === 'trader' ? <TraderPage logout={handleLogoutEvent} /> :  <Navigate to="/login" />}
/>
        <Route 
        path="/transactions/search"
        element={state==='loggedIn' && userType === 'manager' ? <ManagerSearch logout={handleLogoutEvent} /> :  <Navigate to="/login" />}
        />

    </Routes>
);
}


export default App;
