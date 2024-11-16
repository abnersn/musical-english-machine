import { hasAuthorizationError } from '../../utils';

export default function Authorize() {
  if (hasAuthorizationError()) {
    return (
      <section>
        <h2>⚠️ Erro ao autorizar Spotify</h2>
      </section>
    );
  }
  return (
    <section>
      <h2>Autorizar Spotify</h2>
      <p>
        Para começar, precisamos da sua autorização para acessar as músicas que
        você tem ouvido no Spotify.
      </p>
      <form action="/api/authorize" method="get">
        <button type="submit">Clique aqui para autorizar</button>
      </form>
    </section>
  );
}
