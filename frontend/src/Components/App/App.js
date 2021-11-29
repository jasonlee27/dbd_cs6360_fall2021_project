import "./App.css";
import Login from "../Login/Login.js";
import Signup from "../Signup/Signup.js";
import Request from "axios-react";
import React, {useEffect} from 'react';
import useState from 'react-usestateref';

function App() {
  const [isLogin, setIsLogin] = useState('login');
  let handleCreateNewAccount = () => {
    setIsLogin('signup');
  };
  useEffect(() => {
  });

  return (
    <div>
     {isLogin==='login' && 
        <Login createNewAccount={handleCreateNewAccount}/>
      }
      {isLogin==='signup' && 
        <Signup />}
    </div>
  )
}


export default App;
