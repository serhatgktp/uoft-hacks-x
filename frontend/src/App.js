import './App.css';
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

import { Form, useFormik } from "formik";

import Box from '@mui/material/Box';
import { Button } from '@mui/material';
import Fade from '@mui/material/Fade';
import OutlinedCard from './cardComp'
// import SendIcon from '@mui/icons-material/Send';
import TextField from '@mui/material/TextField';
import send_icon from './assets/sent.png'
import { useState } from 'react';

function App() {
  const [json,setJson] = useState({})
  const [submit, setSubmit] = useState(false);
  const formik = useFormik({
    initialValues: {
      p: '',
    },
    onSubmit: (values) => {
      fetch("http://localhost:5000/", {
        method: "POST",
        body: JSON.stringify({topic : values.p}),
        headers: { "Content-Type": "application/json" },
      })
        .then((res) => res.json())
        .then((data) => {
          console.log(data);
        });
    },
  });
  return (
  
   
    
    <div className="App">
    
      <header className="App-header">
        <p id='header-title'>Controversy.io</p>
      </header>
      <div className='main-container'>
        <h1 id="controversy-title">Co:ntroversy</h1>
        <h3 id="sub-title">Access all sides of the argument, delivered by AI</h3>
         {/* <Fade in={submit === false} timeout={2000}>
         <form className="topic-form" action="/action_page.php">
         <Box>
         <TextField id="outlined-basic"  variant="standard" sx={{bgcolor:"white", mx:3, width: '20vw'}} />   
         <Button variant="contained" size="small"  onClick={()=>setSubmit(true)} disabled={!setSubmit}> submit 
         </Button>
         </Box>
         </form> 
         </Fade> */}
        
        {!submit &&<Box>
        {/* <Form onSubmit={formik.handleSubmit}>
        <TextField id="outlined-basic"  name="prompt"  type="prompt" variant="standard" sx={{bgcolor:"white", mx:3, width: '20vw'}} onChange={formik.handleChange}/>   
        <Button variant="contained" size="small"  onClick={()=>{setSubmit(true); 
                  }} disabled={!setSubmit} type="submit"> submit 
        </Button>
        </Form> */}
      
      <form onSubmit={formik.handleSubmit}>
       <input
         id="p"
         name="p"
         type="text"
         onChange={formik.handleChange}
         value={formik.values.p}
       />
       <button type="submit">Submit</button>
       </form>
        </Box> }
         
        
       
      </div>
      
      <Box sx = {{display: 'flex', mt : '5vh', justifyContent: 'center', alignContent: 'center'}}>
          <OutlinedCard></OutlinedCard>
          <OutlinedCard></OutlinedCard>
          <OutlinedCard></OutlinedCard>
        </Box>
    </div>

  )
}

export default App;
