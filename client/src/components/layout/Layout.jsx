import React from "react";
import Header from "./header";
import Footer from "./footer";
import { Link } from "react-router-dom";

const Layout = ({ children }) => {
  return (
    <div>
      <Header />
      {/* <Link>GRn</Link> */}
      <main className="content">{children}</main>
      <Footer />
    </div>
  );
};

export default Layout;
