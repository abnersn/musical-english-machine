import Step from './components/Step';
import { hasTokenRequestCode } from './utils';

function App() {
  return (
    <main>
      <h1>Musical English Machine</h1>
      <Step title="Autorizar Spotify" complete={hasTokenRequestCode()}>
        <p>
          Para começar, precisamos da sua autorização para acessar as músicas
          que você tem ouvido no Spotify.
        </p>
        <form action="/api/authorize" method="get">
          <button type="submit">Clique aqui para autorizar</button>
        </form>
      </Step>
    </main>
  );
}

export default App;
