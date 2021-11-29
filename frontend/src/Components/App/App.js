import "./App.css";
import Login from "../Login/Login.js";
import Signup from "../Signup/Signup.js";
import Transaction from "../btcTransaction.js";
import React, {useEffect} from 'react';
import useState from 'react-usestateref';

function App() {
  const [state, setState] = useState('login');
  let handleCreateNewAccount = () => {
    setState('signup');
  };
  let handleReturnToLogin  = () => {
    setState('login');
  };
  let handleLogin  = () => {
    setState('btcTransaction');
  };

  return (
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
}


export default App;
