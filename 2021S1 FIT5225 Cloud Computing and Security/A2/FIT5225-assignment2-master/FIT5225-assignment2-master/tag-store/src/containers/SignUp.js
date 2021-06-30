import React, { useState } from 'react';
import { Typography, Box, Button, TextField } from '@material-ui/core';
import { useFormFields } from '../libs/hooksLib'
import { Auth } from 'aws-amplify'
import { useAppContext } from '../libs/contextLib'
import { useHistory } from 'react-router-dom'

export default function SignUp() {
    const [fields, handleFieldChange] = useFormFields({     // custom hook to handle form field values
        userName: "",
        firstName: "",
        lastName: "",
        password: "",
        confirmPassword: "",
        confirmationCode: ""
    })

    const [newUser, setNewUser] = useState(null)    // user object
    const { userHasAuthenticated } = useAppContext()
    const history = useHistory()

    // handle registration click button
    async function handleRegisterClick(e) {
        e.preventDefault()
        if (fields.userName.length === 0 || fields.firstName.length === 0 || fields.lastName.length === 0 || fields.password.length === 0 || fields.confirmPassword.length === 0) {
            alert("All fields are mandatory, please fill in all fields")
        } else {
            if (fields.password !== fields.confirmPassword) {
                alert("Passwords don't match")
            } else {
                try {
                    const newUser = await Auth.signUp({
                        username: fields.userName,
                        password: fields.password,
                        attributes: {
                            email: fields.userName,
                            given_name: fields.firstName,
                            family_name: fields.lastName
                        }
                    })
                    setNewUser(newUser)
                } catch (err) {
                    alert("Your password must contain a special character, a capital letter, and a number minimum")
                }
            }
        }
    }

    // handle confirmation submit
    async function handleConfirmationCodeSubmit(e) {
        e.preventDefault()
        try {
            await Auth.confirmSignUp(fields.userName, fields.confirmationCode)
            await Auth.signIn(fields.userName, fields.password)
            userHasAuthenticated(true)
            alert("Registration successful! Redirecting to main menu")
            history.push("/Navigation")
        } catch (error) {
            alert(error)
        }
    }

    // render registration form
    function renderRegistrationForm() {
        return (
            <Box flexGrow={1} display="flex" alignItems="center" flexDirection="column" top="40%" left="25%" right="25%" position="absolute" mx="auto">
                <Typography variant="h2">Register</Typography>
                <TextField
                    id="filled-basic"
                    label="Email"
                    variant="filled"
                    name="userName"
                    required={true}
                    value={fields.userName}
                    onChange={handleFieldChange}
                />
                <TextField
                    id="filled-basic"
                    label="First Name"
                    variant="filled"
                    name="firstName"
                    required={true}
                    value={fields.firstName}
                    onChange={handleFieldChange}
                />
                <TextField
                    id="filled-basic"
                    label="Last Name"
                    variant="filled"
                    name="lastName"
                    required={true}
                    value={fields.lastName}
                    onChange={handleFieldChange}
                />
                <TextField
                    id="filled-password-input"
                    label="Password"
                    type="password"
                    autoComplete="current-password"
                    variant="filled"
                    name="password"
                    required={true}
                    value={fields.password}
                    onChange={handleFieldChange}
                />
                <TextField
                    id="filled-password-input"
                    label="Confirm Password"
                    type="password"
                    autoComplete="current-password"
                    variant="filled"
                    name="confirmPassword"
                    required={true}
                    value={fields.confirmPassword}
                    onChange={handleFieldChange}
                />
                <Button variant="contained" onClick={handleRegisterClick}>Register</Button>
            </Box>
        )
    }

    // render confirmation code form
    function renderConfirmationForm() {
        return (
            <Box flexGrow={1} display="flex" alignItems="center" flexDirection="column" top="40%" left="25%" right="25%" position="absolute" mx="auto">
                <Typography variant="h2">Confirmation Code</Typography>
                <TextField
                    id="filled-basic"
                    label="Enter Confirmation Code"
                    variant="filled"
                    name="confirmationCode"
                    value={fields.confirmationCode}
                    onChange={handleFieldChange}
                />
                <Button variant="contained" onClick={handleConfirmationCodeSubmit}>Submit</Button>
            </Box>
        )
    }

    return (
        <div>
            {newUser === null ? renderRegistrationForm() : renderConfirmationForm()}
        </div>
    )
}