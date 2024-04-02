const CLIENT_ID = import.meta.env.VITE_CLIENT_ID || '{clientId}';
const ISSUER = import.meta.env.VITE_ISSUER;
const OKTA_TESTING_DISABLEHTTPSCHECK = import.meta.env.VITE_OKTA_TESTING_DISABLEHTTPSCHECK || false;
const BASENAME = import.meta.env.VITE_BASE_URL || '';
// BASENAME includes trailing slash
const REDIRECT_URI = `${window.location.origin}${BASENAME}login/callback`;

export default {
  auth0: {
    clientId: CLIENT_ID,
    issuer: ISSUER,
    redirectUri: REDIRECT_URI,
    scopes: ['openid', 'profile', 'email'],
    pkce: true,
    disableHttpsCheck: OKTA_TESTING_DISABLEHTTPSCHECK,
  },
  resourceServer: {
    staffListUrl: 'http://localhost:8000/api/department/staff',
  },
  app: {
    basename: BASENAME,
  },
};