import "./App.css";
import Login from "../Login/Login.js";
import Signup from "../Signup/Signup.js";
import React, {useEffect} from 'react';
import useState from 'react-usestateref';

function App() {
  const [state, setState] = useState('login');
  let handleCreateNewAccount = () => {
    setState('signup');
  };
  let handleLogin  = () => {
    setState('LoggedIn');
  };

  return (
    <div>
     {state==='login' && 
        <Login createNewAccount={handleCreateNewAccount} setLoggedIn={handleLogin}/>
      }
      {state==='signup' && 
        <Signup />}
    </div>
  )
}


export default App;
