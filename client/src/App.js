import './App.css';
import React from 'react';

function App() {
  const [valueA, setValueA] = React.useState(0);

  var jsonData = ["Emily", "take a shower", "college", "Northwestern", "hang out with my friends", "pasta", "finish my homework"]

  function handleClick() {

    // Send data to the backend via POST
    fetch('http://0.0.0.0:8000/generate', {  // Enter your IP address here

      method: 'POST',
      mode: 'cors',
      headers: { 'Content-Type': 'application/json', 'accept': 'application/json' },
      body: JSON.stringify(jsonData) // body data type must match "Content-Type" header
    }).then(response => response.json()).then(data => { console.log(data); setValueA(data.text) });
  }

  return (
    <div>
      <div onClick={handleClick} style={{
        textAlign: 'center',
        width: '100px',
        border: '1px solid gray',
        borderRadius: '5px'
      }}>
        Send data to backend
      </div>
      <div>
        {valueA}
      </div>
    </div>
  );
}

export default App;
