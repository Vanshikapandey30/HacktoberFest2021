import React, { useState } from "react";

export default function TextForm(props) {
  // useState hooks
  const [text, setText] = useState("");

  const [charOccurence, setcharOccurence] = useState(0);

  const handleUpClick = () => {
    let newText = text.toUpperCase();
    setText(newText);
    setcharOccurence(0);
    props.showAlert("Converted to uppercase !","success")
  };

  const handleLowClick = () => {
    let newText = text.toLowerCase();
    setText(newText);
    setcharOccurence(0);
    props.showAlert("Converted to lowercase !","success")
  };

  const handleClearText = () => {
    let newText = "";
    setText(newText);
    setcharOccurence(0);
    props.showAlert("Text Cleared !","success")
  };

  const handleCharOccur = () => {
    let Occur = prompt("Enter the alphabet to find Occurences");
    const myArr = text.split("");
    let count = 0;
    let i = 0;
    for (i = 0; i < myArr.length; i++) {
      //console.log(myArr[i]);
      if (myArr[i] === `${Occur}`) {
        count = count + 1;
      }
    }
    setcharOccurence(count);
    // console.log(count);
  };
    
    const handleOnChange = (event) => {
      setText(event.target.value);
      setcharOccurence(0);
  };

  return (
    <div>
      <div className="container my-4">
        <h2>{props.heading}</h2>
        <div className="mb-3">
          <textarea
            className="form-control"
            id="UserText"
            style={{
              backgroundColor: props.mode === "dark" ? "#212529" : "white",
              color: props.mode === "dark" ? "white" : "black",
            }}
            value={text}
            onChange={handleOnChange}
            rows="9"
            placeholder="Enter Text Here"
          ></textarea>
        </div>

        <button disabled={text.length===0}
          className="btn btn-outline-danger mx-3 my-3"
          onClick={handleUpClick}
        >
          Convert to Uppercase
        </button>

        <button disabled={text.length===0}
          className="btn btn-outline-danger mx-3 my-3"
          onClick={handleLowClick}
        >
          Convert to Lowercase
        </button>

        <button disabled={text.length===0}
          className="btn btn-outline-danger mx-3 my-3"
          onClick={handleClearText}
        >
          Clear Text
        </button>

        <button disabled={text.length===0}
          className="btn btn-outline-danger mx-3 my-3"
          onClick={handleCharOccur}
        >
          Character Occurences
        </button>
      </div>
      <div className="container my-3">
        <h2>All About Text</h2>
        <p>
          <b> {text.trim().split("/\s+/").filter((element)=>{return element.length!==0}).length} </b>
          Words AND
          <b> {text.trim().length} </b>
          Characters
        </p>
        <p>
          Character you searched for Comes <b> {charOccurence}</b> Times
        </p>
        <p>
          It will take about
          <b> {0.08 * text.trim().split("/\s+/").filter((element)=>{return element.length!==0}).length} </b>
          Minutes to read.
        </p>
        <h3 className="my-3">Preview</h3>
        <p>
          {text.length > 0 ? text : "Enter Some Text Above To Preview It Here"}
        </p>
      </div>
    </div>
  );
}

// let str = "How are you doing today?";
// const myArr = str.split("");
// let count=0;
// let i = 0;
// for(i=0;i<myArr.length;i++){
// 	//console.log(myArr[i]);
//     if(myArr[i]==='a'){
// 		count=count+1;
//         //return count;
//         }
// console.log(count);
// }