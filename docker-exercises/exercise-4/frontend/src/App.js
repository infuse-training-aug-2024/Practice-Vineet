import React, { useState, useEffect } from 'react';
import './App.css';
require('dotenv').config();

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Fetching data from the backend API
    fetch(process.env.LOCAL_URL)
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error('Error fetching data:', error));
  }, []); // Empty array means this will run only once when the component mounts

  return (
    <div className="App">
      <header className="App-header">
        <p>This is Vineet</p>
        <p>{message ? message : "Loading..."}</p>
      </header>
    </div>
  );
}

export default App;
