import './App.css';
import '@fontsource/roboto/300.css';
import '@fontsource/roboto/400.css';
import '@fontsource/roboto/500.css';
import '@fontsource/roboto/700.css';

import Box from '@mui/material/Box';
import { Button } from '@mui/material';
// import SendIcon from '@mui/icons-material/Send';
import TextField from '@mui/material/TextField';
import send_icon from './assets/sent.png'
import { useState } from 'react';

function App() {
  const [json,setJson] = useState({})
  const [submit, setSubmit] = useState(false);
  return (
    <div className="App">
      <header className="App-header">
        <p id='header-title'>controversy.io</p>
      </header>
      <div className='main-container'>
        <h1 id="controversy-title">Co:ntroversy</h1>
        <h3 id="sub-title">Access all sides of the argument, delivered by AI</h3>
        <form className="topic-form" action="/action_page.php">
        
       
        <TextField id="outlined-basic"  variant="standard" sx={{bgcolor:"white", mx:3}} />
        <Button variant="contained" size="small" > submit </Button>
        
        </form> 
      </div>
    </div>
  );
}

export default App;
