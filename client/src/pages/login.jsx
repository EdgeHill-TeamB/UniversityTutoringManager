import { useEffect } from "react";
import { useAuth0 } from "@auth0/auth0-react";

export default function Login() {
  const { loginWithRedirect } = useAuth0();
  useEffect(() => {
    loginWithRedirect();
  }, []);
  return (
    <div>
      <h1>Login</h1>
      <p>This is the login page.</p>
    </div>
  );
}
