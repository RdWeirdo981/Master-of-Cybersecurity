import React from "react";
import { Typography, Box } from '@material-ui/core';


export default function Home() {
  return (
    <Box position="absolute" top="40%" left="40%" right="40%">
      <Typography variant="h1">Tag Store</Typography>
      <Typography variant="h4">An image recognition service</Typography>
    </Box>
  );
}