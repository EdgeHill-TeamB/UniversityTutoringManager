import React from "react";
import { Route, Routes, BrowserRouter } from "react-router-dom";
import config from "./config.js";
import Layout from "./components/layout/Layout.jsx";

// Pages
import DepAdminPage from "./pages/dep_admin.jsx";
// Pages End

import "/src/styles/App.css";
import RequireAuth from "./routeProtectors/requireAuth.jsx";
import Login from "./pages/login.jsx";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route element={<RequireAuth />}>
          <Route path="/dep_admin" element={<DepAdminPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
