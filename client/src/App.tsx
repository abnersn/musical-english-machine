import React from 'react';

function App() {
  const handleClickAuthenticate = () => {
    console.log('auth');
  };
  return (
    <main>
      <h1>Musical English Machine</h1>
      <section>
        <h2>Spotify</h2>
        <button onClick={handleClickAuthenticate}>
          Click here to authenticate
        </button>
      </section>
    </main>
  );
}

export default App;
