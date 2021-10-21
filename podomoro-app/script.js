(function () {
    // DOM Elements
    var pomodoro = document.getElementById("pomodoro");
    var firstBtn = document.getElementById("first-btn");
    var secondBtn = document.getElementById("second-btn");
    var minElem = document.getElementById("min");
    var secElem = document.getElementById("sec");
  
    // Variables
    var min = 25;
    var sec = 0;
    var interv = null;
    var isRest = false;
  
    // events
    firstBtn.addEventListener("click", firstBtnClickHandler);
    secondBtn.addEventListener("click", rest);
  
    // handlers
    function firstBtnClickHandler(e) {
      secondBtn.disabled = false;
  
      if (firstBtn.innerHTML === "pause") {
        firstBtn.innerHTML = "resume";
        if (secondBtn.innerHTML !== "skip") secondBtn.innerHTML = "done";
        clearInterval(interv);
      } else {
        firstBtn.innerHTML = "pause";
        if (secondBtn.innerHTML !== "skip") secondBtn.innerHTML = "stop";
        timer();
      }
    }
  
    // helper functions
    function timer() {
      interv = setInterval(function () {
        sec--;
        if (sec < 0) {
          min--;
          if (min < 0) {
            rest();
          } else {
            sec = 59;
  
            // set Minutes in the DOM
            changeTimeUi(minElem, min);
          }
        }
        // set seconds in the DOM
        changeTimeUi(secElem, sec);
      }, 1000);
    }
  
    function changeTimeUi(elem, time) {
      var str = time + "";
      if (str.length === 1) str = "0" + str;
      elem.innerHTML = str;
    }
  
    function rest() {
      // set min and sec
      min = isRest ? 25 : 5;
      sec = 0;
      minElem.innerHTML = isRest ? min : "0" + min;
      secElem.innerHTML = "0" + sec;
  
      // pomodoro color
      if (isRest) {
        pomodoro.classList.remove("rest");
      } else {
        pomodoro.classList.add("rest");
      }
  
      // buttons labels
      firstBtn.innerHTML = isRest ? "start" : "pause";
      secondBtn.innerHTML = isRest ? "stop" : "skip";
      secondBtn.disabled = isRest;
  
      // timer
      clearInterval(interv);
      interv = null;
      if (!isRest) {
        timer();
      }
      isRest = !isRest;
    }
  })();
  