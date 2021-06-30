import React from 'react';
import { Typography, Box } from '@material-ui/core';
import { Button } from '@material-ui/core';
import { TextField } from '@material-ui/core';
import { Auth } from 'aws-amplify';
import { useAppContext } from '../libs/contextLib';
import { useHistory } from 'react-router-dom';
import { useFormFields } from '../libs/hooksLib';

export default function SignIn() {
    const [fields, handleFieldChange] = useFormFields({     // custom hook for form fields
        userName: "",
        password: ""
    })
    const { userHasAuthenticated } = useAppContext()    // use hook to update state and pass to context
    const history = useHistory()

    async function handleSignIn(e) {
        e.preventDefault()
        if (fields.userName.length === 0 || fields.password.length === 0) {
            alert("Username or password cannot be blank")
        } else {
            try {
                await Auth.signIn(fields.userName, fields.password)
                console.log("Logged In")
                //await Auth.currentSession()
                    //.then(session => {
                      //  console.log(session)
                    //})
                userHasAuthenticated(true)
                history.push("/Navigation")
            } catch (err) {
                console.log(err.message)
            }
        }
    }

    return (
        <Box flexGrow={1} display="flex" alignItems="center" flexDirection="column" top="40%" left="25%" right="25%" position="absolute" mx="auto">
            <Typography variant="h2">Login</Typography>
            <TextField
                id="filled-basic"
                label="Email"
                variant="filled"
                name="userName"
                value={fields.userName}
                onChange={handleFieldChange}
            />
            <TextField
                id="filled-password-input"
                label="Password"
                type="password"
                autoComplete="current-password"
                variant="filled"
                name="password"
                value={fields.password}
                onChange={handleFieldChange}
            />
            <Button
                variant="contained"
                href="/"
                onClick={handleSignIn}
            >Sign In</Button>
        </Box>
    );
}