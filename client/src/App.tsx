import Authorize from './components/Authorize';
import Progress from './components/Progress';
import { hasTokenRequestCode } from './utils';

function App() {
  return (
    <main>
      <h1>Musical English Machine</h1>
      {!hasTokenRequestCode() && <Authorize />}
      {hasTokenRequestCode() && <Progress />}
    </main>
  );
}

export default App;
