import React from 'react';
import { makeStyles } from '@material-ui/core/styles'
import { Paper, MenuList, MenuItem, Typography } from '@material-ui/core';
import { useHistory } from 'react-router-dom';
import { createBrowserHistory } from 'history';

const history = createBrowserHistory();

const path = (/#!(\/.*)$/.exec(window.location.hash) || [])[1];
if (path) {
    history.replace(path);
}

const useStyles = makeStyles((theme) => ({
    root: {
        display: 'flex',
        justifyContent: 'center',
        flexDirection: 'column',
        alignItems: 'center'
    },
    paper: {
        marginRight: theme.spacing(2)
    }
}))

export default function Navigation() {
    const classes = useStyles();
    const history = useHistory();

    function handleUploadClick(e) {
        console.log("clicked");
        history.push("/Upload");
    }

    function handleQueryClick(e) {
        console.log("clicked");
        history.push("/Query");
    }

    return (
        <div className={classes.root}>
            <Typography variant="h6" >Navigation Menu</Typography>
            <br />
            <Paper>
                <MenuList>
                    <MenuItem onClick={handleUploadClick}>Upload Image</MenuItem>
                    <MenuItem onClick={handleQueryClick}>Query Image</MenuItem>
                </MenuList>
            </Paper>
        </div>
    );
}
