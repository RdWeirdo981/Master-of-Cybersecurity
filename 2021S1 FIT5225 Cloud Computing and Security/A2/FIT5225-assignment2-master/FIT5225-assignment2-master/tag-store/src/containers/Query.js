import React from 'react';
import { Typography, Box, Button, TextareaAutosize } from '@material-ui/core';
import { useHistory } from 'react-router-dom'
import { Auth } from 'aws-amplify';
import axios from 'axios';

export default function Query() {
  const history = useHistory();

  let params = [];
  let tagArray = [];
  let resData = [];

  function handleBackClick(e) {
    history.push("/Navigation");
  }

  function handleTextChange(e) {
    tagArray = e.target.value.split(",");
    if (tagArray.length > 10) {
      alert("Only 10 tags allowed");
    }
    // console.log(tagArray)
    return tagArray;
  }

  async function generateTags() {
    if (tagArray.length === 0) {
      alert("Please enter at least one tag")
      return;
    }
    var count = 1;
    tagArray.forEach(element => {
      let tag = "tag" + count;
      let param = { [tag]: element };
      params.push(param);
      count++;
      // console.log(params)
    })

    const idToken = await (await Auth.currentSession()).getIdToken()
    console.log("idToken: ", idToken);
    let options = '';
    params.forEach(param => {
      const key = Object.keys(param)[0];
      const value = Object.values(param)[0];
      options += `${key}=${value}&`;
    })
    params = [];
    tagArray = [];
    document.getElementById("tags").value = "";
    options = options.slice(0, -1);
    console.log(options);


    const url = "https://7wo7odchxb.execute-api.us-east-1.amazonaws.com/dev/search?" + options;
    // axios.get(url)
    //   .then(res => {
    //     console.log("response", res)
    //   })

    axios({
      method: "GET",
      url: url,
      headers: {
        Authorization: "Bearer " + idToken.getJwtToken()
      },
    })
      .then(res => {
        console.log("response", res)
        resData = res.data
        console.log(resData)
        document.getElementById("results").value = JSON.stringify(resData,null,3)
      })
      .catch(err => {
        console.log("Error", err)
      })

  }

  return (
    <Box display="flex" alignItems="center" flexDirection="column" top="5%" left="25%" right="25%" position="absolute" mx="auto">
      <Typography variant="h1">Run Query</Typography>
      <TextareaAutosize rowsMin={3} placeholder="Enter tags seperated by ','" id="tags" onChange={handleTextChange.bind(this)} />
      <Button variant="contained" onClick={generateTags}>Execute</Button>
      <Button variant="contained" onClick={handleBackClick}>Back</Button>
      <Box display="flex" alignItems="center" flexDirection="column" top="100%" left="25%" right="25%" position="absolute" mx="auto" width={100}>
      <TextareaAutosize rowsMin={3} placeholder="Results will be displayed here, drag corner as needed" id="results" width={100}/>
      </Box>
    </Box>
  );
}