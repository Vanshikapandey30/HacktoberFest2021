import React from "react";
import PropTypes from "prop-types";
// import { Link } from "react-router-dom";
// import { Link } from "react-router-dom";

export default function Navbar(props) {

  return (
    <div>
      <nav
        className={`navbar navbar-expand-lg navbar-${props.mode} bg-${props.mode}`}
      >
        <div className="container-fluid">
          <a className="navbar-brand" href="/">
            {props.AppName}
          </a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarSupportedContent">
            <ul className="navbar-nav me-auto mb-2 mb-lg-0">
              <li className="nav-item">
                <a className="nav-link active" aria-current="page" href="/">
                  Home
                </a>
              </li>
              {/* <li className="nav-item">
                <Link className="nav-link" to="/about">
                  {props.AboutPage}
                </Link>
              </li> */}
            </ul>
            <div onClick={props.colorChange} className="colorPallets mx-3">
              <input type="color" id="colorpicker" />
            </div>
            <div className="form-check form-switch">
              <input
                className="form-check-input"
                type="checkbox"
                id="flexSwitchCheckDefault"
                onClick={props.toggleMode}
              />
              <label
                className={`form-check-label text-${
                  props.mode === "light" ? "dark" : "light"
                }`}
                htmlFor="flexSwitchCheckDefault"
              >
                {props.ModeLabel}
              </label>
            </div>
          </div>
        </div>
      </nav>
    </div>
  );
}

Navbar.propTypes = {
  AppName: PropTypes.string.isRequired,
  AboutPage: PropTypes.string.isRequired,
};

Navbar.defaultProps = {
  AppName: "set app name here",
  AboutPage: "set about text here",
};