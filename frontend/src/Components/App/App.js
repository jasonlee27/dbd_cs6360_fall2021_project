import "./App.css";
import Login from "../Login/Login.js";
import Signup from "../Signup/Signup.js";
import Request from "axios-react";
import React, { useState, useEffect } from 'react'

function App() {
  const [isLogin, setIsLogin] = useState(true);
  let handleCreateNewAccount = () => {
    setIsLogin(false);
  };

  return (
    <div>
     {isLogin && (
        <Login createNewAccount={handleCreateNewAccount}/>
      )}
      {!isLogin && (
        <Signup />
      )}
    </div>

  )
}


export default App;
