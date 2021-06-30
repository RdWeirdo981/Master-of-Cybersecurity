import React from 'react';
import { Typography, Box, Button } from '@material-ui/core';
import { Storage } from "aws-amplify";
import { useHistory } from 'react-router-dom';

export default function Upload() {

 var filename = '';
 var file = '';

 function handleChange(e){
   file = e.target.files[0];
   filename = file.name;
 }

 function save(){
   if (filename != "") {
   Storage.put(filename, file)
    .then(() => {
      console.log('Upload success');
      filename = '';
      file='';
      history.push("/Navigation");
    })
    .catch(err => {
      console.log(err);
    })
  }
  else {
    alert("Please select a file to upload");
  }
 }

  const history = useHistory();

  function handleBackClick(e) {
    history.push("/Navigation");
  }

  return (
    <Box display="flex" alignItems="center" flexDirection="column" top="40%" left="25%" right="25%" position="absolute" mx="auto">
      <Typography variant="h1">Upload an Image</Typography>
      <input type="file" onChange={handleChange} />
      <Button variant="contained" onClick={save}>Upload</Button>
      <Button variant="contained" onClick={handleBackClick}>Back</Button>
    </Box>
  );


}

