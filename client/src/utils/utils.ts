export const hasTokenRequestCode = () =>
  Boolean(
    new URLSearchParams(window.location.search).get('token_request_code')
  );
