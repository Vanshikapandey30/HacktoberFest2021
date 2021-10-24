// import logo from "./logo.svg";
import React, { useState } from "react";
import "./App.css";
import Alert from "./Components/Alert";
import Navbar from "./Components/Navbar";
import TextForm from "./Components/TextForm";
// import About from "./Components/About";
// import { BrowserRouter as Router, Switch, Route } from "react-router-dom";

function App() {
  const [mode, setMode] = useState("light");
  const [modeLabel, setModeLabel] = useState("Enable Dark Mode");
  const [alert, setAlert] = useState(null);

  const colorChange = () => {
    let colour = document.getElementById("colorpicker").value;
    document.body.style.backgroundColor = colour;
  };

  const showAlert = (message, type) => {
    setAlert({ msg: message, type: type });
    setTimeout(() => {
      setAlert(null);
    }, 2000);
  };

  const toggleMode = () => {
    if (mode === "light") {
      setMode("dark");
      setModeLabel("Enable Light Mode");
      document.body.style.backgroundColor = "#212529";
      document.body.style.color = "#fff";
      showAlert("Dark mode has been enabled.", "success");
      // this is for dynamically changing the title of the website.
      document.title = "TextLab | Dark Mode";
    } else {
      setMode("light");
      setModeLabel("Enable Dark Mode");
      document.body.style.backgroundColor = "white";
      document.body.style.color = "black";
      showAlert("Light mode has been enabled.", "success");
    }
  };

  return (
    <>
      {/* <Router> */}
        <Navbar
          AppName="TextLab"
          AboutPage="About Us"
          mode={mode}
          colorChange={colorChange}
          toggleMode={toggleMode}
          ModeLabel={modeLabel}
        />
        {/* here we are passing the useState alert to alert.js as a prop */}
        <Alert alert={alert} />
        {/* <Switch> */}
          {/* <Route exact path="/about"> */}
            {/* <About mode={mode} /> */}
          {/* </Route> */}
          {/* <Route exact path="/"> */}
            <TextForm
              showAlert={showAlert}
              heading="Enter The Text Below"
              mode={mode}
            />
          {/* </Route> */}
        {/* </Switch> */}
      {/* </Router> */}
    </>
  );
}

export default App;