import React, { useState, useEffect } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';
import Routes from "./Routes";
import { AppContext } from './libs/contextLib';    // using context to get state from different components
import { Auth } from "aws-amplify";
import { createBrowserHistory } from 'history';

const history = createBrowserHistory();

const path = (/#!(\/.*)$/.exec(window.location.hash) || [])[1];
if (path) {
    history.replace(path);
}


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

export default function App() {
  const classes = useStyles();
  const [isAuthenticating, setIsAuthenticating] = useState(true)    // load state from session
  const [isAuthenticated, userHasAuthenticated] = useState(false)   // add session to state

  // similar to componentDidMount in classes
  // second parameter empty list implies function passed will run only on the FIRST render
  // i.e. when the app first loads, to check the auth from user session
  useEffect(() => {
    console.log("isAuthenicated", isAuthenticated)
    console.log("isAuthenticating", isAuthenticating)
    onLoad()
  }, [])

  async function onLoad() {
    try {
      await Auth.currentSession()
      userHasAuthenticated(true)
    } catch (e) {
      if (e !== 'No current user') {
        alert(e)
      }
    }
    setIsAuthenticating(false)
  }

  // handle logout, logout button appears after sign in
  async function handleLogout(e) {
    // e.preventDefault()
    await Auth.signOut()
    userHasAuthenticated(false)
  }

  return (
    !isAuthenticating &&
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Tag Store
          </Typography>
          {/* <Button color="inherit" onClick={handleCheckState}>Check State</Button> */}
          {isAuthenticated
            ? <Button color="inherit" href="/" onClick={handleLogout}>Logout</Button>
            : <>
              <Button color="inherit" href="/SignIn">Sign In</Button>
              <Button color="inherit" href="/SignUp">Sign Up</Button>
            </>
          }
        </Toolbar>
      </AppBar>
      <AppContext.Provider value={{ isAuthenticated, userHasAuthenticated }}>
        <Routes />
      </AppContext.Provider>
    </div>
  );
}