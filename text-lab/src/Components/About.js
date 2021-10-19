import React from "react";          // , { useState }

export default function About(props) {
  
  // const [btnText, setbtnText] = useState('Enable Dark Mode');

  
  // const [darkMode, setdarkMode] = useState({
  //   backgroundColor: "white",
  //   color: "black",
  // });

  // const toggleStyle = () => {
  //   if (darkMode.color === "black") {
  //     setdarkMode({
  //       backgroundColor: "grey",
  //       color: "white",
  //     });

  //     setbtnText('Enable Light Mode');

  //   } else {
  //     setdarkMode({
  //       backgroundColor: "white",
  //       color: "black",
  //     });
  //     setbtnText('Enable Dark Mode');
  //   }
  // };

  const darkMode = {
    color:props.mode==='dark'?'white':'#212529',
    backgroundColor:props.mode==='dark'?'#212529':'white',
    border: '2px solid white'
  }

  return (
    <div >
      <div className="container my-4" >
        <h1 className="my-2">About Us</h1>
        <div className="row">
          <div className="col-sm-6">
            <div className="card" style={darkMode}>
              <div className="card-body">
                <h5 className="card-title">Special title treatment</h5>
                <p className="card-text">
                  With supporting text below as a natural lead-in to additional
                  content.
                </p>
                <a href="/" className="btn btn-primary">
                  Go somewhere
                </a>
              </div>
            </div>
          </div>
          <div className="col-sm-6">
            <div className="card" style={darkMode}>
              <div className="card-body">
                <h5 className="card-title">Special title treatment</h5>
                <p className="card-text">
                  With supporting text below as a natural lead-in to additional
                  content.
                </p>
                <a href="/" className="btn btn-primary">
                  Go somewhere
                </a>
              </div>
            </div>
          </div>
        </div>
        {/* <button
          onClick={toggleStyle}
          id="modeBtn"
          className="btn btn-outline-danger my-3"
        >
          {btnText}
        </button> */}
      </div>
    </div>
  );
}