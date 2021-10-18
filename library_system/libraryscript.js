// Preloader
(() => {
    window.addEventListener("load", function() {
        document.querySelector(".preloader").classList.add("opacity-0");
        setTimeout(function() {
            document.querySelector(".preloader").style.display = "none";
        }, 1000);
    });
})();

console.log('This is ITSOURCECODE Project');
class Library {
    constructor(name, author, type, price) {
        this.name = name;
        this.author = author;
        this.type = type;
        this.price = price;
    }
}

class Display {
    add(bookoflibrary) {
        console.log("Adding to UI");
        let tableBody = document.getElementById('tableBody');
        let uiString = `<tr>
                            <td>${bookoflibrary.name}</td>
                            <td>${bookoflibrary.author}</td>
                            <td>${bookoflibrary.type}</td>
                            <td>${bookoflibrary.price}</td>
                        </tr>`;
        tableBody.innerHTML += uiString;
    }
    fv

    clear() {
        let libraryForm = document.getElementById('libraryForm');
        libraryForm.reset();
    }

    validate(bookoflibrary) {
        if (bookoflibrary.name.length < 2 || bookoflibrary.author.length < 2) {
            return false
        } else {
            return true;
        }
    }

    show(type, displayMessage) {
        let message = document.getElementById('message');
        let boldText;
        if (type === 'success') {
            boldText = 'Success';
        } else {
            boldText = 'Error!';
        }
        message.innerHTML = `<div class="alert alert-${type} alert-dismissible fade show" role="alert">
                                <strong>${boldText}:</strong> ${displayMessage}
                                <button type="button" class="close" data-dismiss="alert" aria-label="Close">
                                <span aria-hidden="true">×</span>
                                </button>
                            </div>`;
        setTimeout(function() {
            message.innerHTML = ''
        }, 5000);

    }
}

// Add submit event listener to libraryForm
let libraryForm = document.getElementById('libraryForm');
libraryForm.addEventListener('submit', libraryFormSubmit);


let clearData = document.getElementById('clearData');
clearData.addEventListener('submit', clearAllData);


function clearAllData(e) {
    let display = new Display();
    display.clear();
    console.log('data cleared');

}

function libraryFormSubmit(e) {
    console.log('You have submitted library form');
    let name = document.getElementById('bookName').value;
    let author = document.getElementById('author').value;
    let type;
    let philippine = document.getElementById('philippine');
    let programming = document.getElementById('programming');
    let science = document.getElementById('science');
    let price = document.getElementById('price').value;

    if (philippine.checked) {
        type = philippine.value;
    } else if (programming.checked) {
        type = programming.value;
    } else if (science.checked) {
        type = science.value;
    }

    let bookoflibrary = new Library(name, author, type, price);
    console.log(bookoflibrary);

    let display = new Display();

    if (display.validate(bookoflibrary)) {

        display.add(bookoflibrary);
        display.clear();
        display.show('success', 'Your book has been successfully added')
    } else {
        // Show error to the user
        display.show('danger', 'Sorry you cannot add this book');
    }

    e.preventDefault();
}
