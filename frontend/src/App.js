import './App.css';
import send_icon from './assets/sent.png'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p id='header-title'>controversy.io</p>
      </header>
      <div className='main-container'>
        <h1 id="controversy-title">co:ntroversy</h1>
        <h3 id="sub-title">Access all sides of the argument, delivered by AI</h3>
        <form className="topic-form" action="/action_page.php">
          <input type="text" id="topic-textbox" name="topic" />
          <img id="send_icon" alt="send-icon" src={send_icon} target=""/>
        </form> 
      </div>
    </div>
  );
}

export default App;
