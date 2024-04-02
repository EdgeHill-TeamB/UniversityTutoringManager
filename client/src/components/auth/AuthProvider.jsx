import React, { useContext, createContext, useState } from "react";
import { useNavigate } from "react-router-dom";

// Create a context for the auth state
const AuthContext = createContext();

// Create a provider component
export function AuthProvider({ children }) {
  const navigate = useNavigate();
  const [authToken, setAuthToken] = useState(null);

  // Check if the user is authenticated
  if (!authToken) {
    // Redirect to the external auth page
    navigate("/auth");
  }

  return (
    <AuthContext.Provider value={{ authToken, setAuthToken }}>
      {children}
    </AuthContext.Provider>
  );
}

// Create a hook to use the auth context
export function useAuth() {
  return useContext(AuthContext);
}
