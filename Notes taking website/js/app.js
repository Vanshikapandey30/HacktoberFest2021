console.log("welcome to Notes App");
displayNote();
//event Listener for clicking on addnote button

let addbtn = document.getElementById("addbtn");
let addtitlebtn=document.getElementById("titlebtn");
addtitlebtn.addEventListener("click",function(e){
    let txt=document.getElementById("titleinput");
    let title=localStorage.getItem('title');
    let titleObj;
    if(title==null){
        titleObj=[];
    }
    else{
        titleObj=JSON.parse(title);
    }
    titleObj.push(txt.value);
    localStorage.setItem("title",JSON.stringify(titleObj));
    txt.value="";
    console.log("title:- ",titleObj);
    displayNote();


})


addbtn.addEventListener('click', function (e) {
    let txt = document.getElementById("addtxtarea");
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = []
    }
    else {
        notesObj = JSON.parse(notes);
    }
    notesObj.push(txt.value);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    txt.value = "";
    console.log("notes:- ",notesObj);
    displayNote();
});

function displayNote() {
    let notes = localStorage.getItem('notes');
    
    if (notes == null) {
        notesObj = []
    }
    else {
        notesObj = JSON.parse(notes);
    }
    let title=localStorage.getItem('title');
    if (title == null) {
        titleObj = []
    }
    else {
        titleObj = JSON.parse(title);
    }
    let html = "";
    notesObj.forEach(function (element, index) {
        html += `
        <div class="noteCard my-2 mx-2" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title" id="tit"> ${titleObj[index]}</h5>
            <p class="card-text">${element}</p>
            <button id=${index} onclick="deleteNode(this.id)" type="button" class="btn btn-danger">Delete Node</button>
        </div>
    </div> `
    });
   
    let noteselm = document.getElementById("notes");
    if (notesObj.length != 0) {
        noteselm.innerHTML = html;

    }
    else {
        noteselm.innerHTML = `<i>No notes yet! Use 'Add a Note' section above to add
                               notes which will be displayed here.</i>`;
    }
    

}

function deleteNode(index){
    
    //console.log(`Deleting Node ${index}`);
    let notes = localStorage.getItem('notes');
    let title=localStorage.getItem('title');
    if (notes == null) {
        notesObj = []
    }
    else {
        notesObj = JSON.parse(notes);
    }

    if(title==null){
        titleObj=[];
    }
    else{
        titleObj=JSON.parse(title);
    }
    notesObj.splice(index,1);
    titleObj.splice(index,1);
    
    localStorage.setItem("notes", JSON.stringify(notesObj));
    localStorage.setItem("title", JSON.stringify(titleObj));

    displayNote();

}

let search=document.getElementById("searchtxt");
search.addEventListener("input",function(){
    let inputVal=search.value;
    let notecard=document.getElementsByClassName("noteCard");
    Array.from(notecard).forEach(function(element){
        let txt=element.getElementsByTagName("p")[0].innerText;
        let titl=element.getElementsByTagName("h5")[0].innerText;
        if(txt.includes(inputVal) || titl.includes(inputVal)){
            element.style.display="block";
        }
        else{
            element.style.display="none";

        }

    });


})


/*
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width= , initial-scale=1.0">
    <title>Notes App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-KyZXEAg3QhqLMpG8r+8fhAXLRk2vvoC2f3B09zVXn8CA5QIVfZOJ3BCsw2P0p/We" crossorigin="anonymous">
</head>

<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <div class="container-fluid">
            <a class="navbar-brand" href="#">Quick Notes</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
                data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false"
                aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                        <a class="nav-link active" aria-current="page" href="#">Home</a>
                    </li>

                </ul>
                <form class="d-flex">
                    <input class="form-control me-2" id="searchtxt" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            </div>
        </div>
    </nav>

    <div class="container my-3">
        <h1 id="h1">Welcome to Quick Notes!</h1>
        <div class="card" ">
            <div class=" card-body">
            <h5 class="card-title">Add a Note</h5>
            <div class="form-floating">
                <textarea class="form-control" placeholder="Leave a comment here" id="addtxtarea"></textarea>
            </div>
            <button id="addbtn" type="button" class="btn btn-success">Add Note</button>
        </div>
    </div>
    <hr>
    <h1>Your Notes</h1>
    <hr>
    <div id="notes" class="row container-fluid"> </div>

    </div>
    </div>


    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.3/dist/umd/popper.min.js"
        integrity="sha384-eMNCOe7tC1doHpGoWe/6oMVemdAVTMs2xqW4mwXrXsW0L84Iytr2wi5v2QjrP/xp"
        crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.0/dist/js/bootstrap.min.js"
        integrity="sha384-cn7l7gDp0eyniUwwAZgrzD06kc/tftFf19TOAs2zVinnD/C7E91j9yyk5//jjpt/"
        crossorigin="anonymous"></script>
    <script src="js/app.js"></script>
</body>

</html>
*/

/*console.log("welcome to Notes App");
displayNote();
//event Listener for clicking on addnote button

let addbtn = document.getElementById("addbtn");


addbtn.addEventListener('click', function (e) {
    let txt = document.getElementById("addtxtarea");
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = []
    }
    else {
        notesObj = JSON.parse(notes);
    }
    notesObj.push(txt.value);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    txt.value = "";
    console.log(notesObj);
    displayNote();
});

function displayNote() {
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = []
    }
    else {
        notesObj = JSON.parse(notes);
    }
    let html = "";
    notesObj.forEach(function (element, index) {
        html += `
        <div class="noteCard my-2 mx-2" style="width: 18rem;">
        <div class="card-body">
            <h5 class="card-title">Note ${index + 1}</h5>
            <p class="card-text">${element}</p>
            <button id=${index} onclick="deleteNode(this.id)" type="button" class="btn btn-danger">Delete Node</button>
        </div>
    </div>
        
        `

    });
    let noteselm = document.getElementById("notes");
    if (notesObj.length != 0) {
        noteselm.innerHTML = html;
    }
    else {
        noteselm.innerHTML = `<i>No notes yet! Use 'Add a Note' section above to add
                               notes which will be displayed here.</i>`;
    }

}

function deleteNode(index){
    
    console.log(`Deleting Node ${index}`);
    let notes = localStorage.getItem('notes');
    if (notes == null) {
        notesObj = []
    }
    else {
        notesObj = JSON.parse(notes);
    }
    notesObj.splice(index,1);
    localStorage.setItem("notes", JSON.stringify(notesObj));
    displayNote();

}

let search=document.getElementById("searchtxt");
search.addEventListener("input",function(){
    let inputVal=search.value;
    let notecard=document.getElementsByClassName("noteCard");
    Array.from(notecard).forEach(function(element){
        let txt=element.getElementsByTagName("p")[0].innerText;
        if(txt.includes(inputVal)){
            element.style.display="block";
        }
        else{
            element.style.display="none";

        }

    });


})
*/