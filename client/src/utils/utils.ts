export const hasTokenRequestCode = () =>
  Boolean(
    new URLSearchParams(window.location.search).get('token_request_code')
  );

export const hasAuthorizationError = () =>
  new URLSearchParams(window.location.search).get('authorization_error') ===
  'true';
