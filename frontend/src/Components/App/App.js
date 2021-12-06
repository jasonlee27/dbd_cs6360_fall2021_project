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
import AssignTrader from "../AssignTrader";

function App() {
  const [state, setState] = useState('login');
  const [userId, setUserID, userIdRef] = useState('');
  const [userType, setUserType, userTypeRef] = useState('');
  const [trader, setTrader, traderRef] = useState('');
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

  async function handleLogoutEvent(e) {
    await axios
      .request("http://localhost:8080/logout")
      .then((response) => {
        if (response.data.msg === "Successfully logged out") {
            handleLogout();
        }
      }).catch((error) => {
        console.log("error", error);
      });
  }

  async function getClientTrader(userId) {
    await axios
    .post("http://localhost:8080/profile/trader_assigned")
    .then((response) => {
      console.log("trader info: ", response.data);
      if (response.data.msg === "No traders") {
        setTrader("");
      }
        else if(response.data.msg === "Successfully captured trader") {
          setTrader(response.data.trader);
        }
      else {
        console.log("No trader");
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
    setUserID(userId);
  await getUserInfo(userId).then((response)=> {
    console.log(userTypeRef.current);
    if(userTypeRef.current==="client"){
      navigate('/transaction');
    getClientTrader(userId).then((response) => {
      console.log("trade data", trader);
      console.log("trade trade ref", traderRef.current);
        if(traderRef.current == null || traderRef.current === "") {
          console.log("null trader");
          navigate('/assign/trader');
        }
        else {
          navigate('/transaction');
        }

    }).catch((error) => {
      console.log("error", error);
    });
    }
    else if(userTypeRef.current==="trader") {
      navigate('/trader')
    }
    else if(userTypeRef.current==="manager") {
      navigate('/transactions/search')
    }
  });
};

function handleClientSelected() {
  setState('loggedIn');
  navigate('/transaction');
}
  
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
        element={state==='loggedIn' && userType === 'trader' ? <TraderPage userId={userIdRef.current} logout={handleLogoutEvent} /> :  <Navigate to="/login" />}
/>
        <Route 
        path="/transactions/search"
        element={state==='loggedIn' && userType === 'manager' ? <ManagerSearch logout={handleLogoutEvent} /> :  <Navigate to="/login" />}
        />
           <Route 
        path="/assign/trader"
        element={state==='loggedIn' && userType === 'client' ? <AssignTrader logout={handleLogoutEvent} goToTransaction={handleClientSelected} /> :  <Navigate to="/login" />} />

    </Routes>
);
}


export default App;
