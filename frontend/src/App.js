import './App.css';
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

import {Box, Typography}  from "@mui/material";

function App() {
  return (
  <Box display={"flex"} alignItems={"center"} justifyContent={"center"} sx={{height:"100vh"}}>
    <Box width= {"900px"} display={"flex"} flexDirection={"column"} justifyContent={"space-between"}>
      <Typography variant='h1' component="h1"> Controvesy.io</Typography>
   </Box>
   </Box>
  );
}

export default App;
