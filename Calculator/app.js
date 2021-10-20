let screen = document.getElementById("screen");

let buttons = document.querySelectorAll("button");

let screenValue = "";

for(item of buttons){
  item.addEventListener("click",function(e){
    let buttonText = e.target.innerText;
    // console.log(buttonText);
    if(buttonText=="C"){
      screenValue = "";
      screen.value = screenValue; //JS function to get value of screen.
    }
    else if(buttonText=="="){
      screen.value = eval(screenValue);  //JS function to evaluate any operation.
    }
    else if(buttonText=="÷"){
      buttonText="/";
      screenValue += buttonText;
      screen.value = screenValue;
    }
    else{
      screenValue += buttonText;
      screen.value = screenValue;
    }

  });
}
