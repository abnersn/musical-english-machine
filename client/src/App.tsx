import React from 'react';

function App() {
  return (
    <main>
      <h1>Musical English Machine</h1>
      <section>
        <h2>Spotify</h2>
        <p>
          Para começar, precisamos da sua autorização para acessar as músicas
          que você tem ouvido no Spotify.
        </p>
        <form action="/api/authorize" method="get">
          <button type="submit">Clique aqui para autorizar</button>
        </form>
      </section>
    </main>
  );
}

export default App;
