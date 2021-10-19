// api key - c569897da01aa711e1df53610eb8f9cf

//var url = 'https://api.openweathermap.org/data/2.5/weather?q=${city.value}&appid=c569897da01aa711e1df53610eb8f9cf&units=metric';
var sub = document.getElementsByClassName("btn-outline-info")[0];
sub.addEventListener("click", getValues);

async function getValues() {
    var city = document.getElementById("search-bar").value; //isko bahar rakhne se click krne par seedha values pe aata tha...city ka name input nhi leta tha
    const response = await fetch('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=c569897da01aa711e1df53610eb8f9cf&units=metric');
    const json = await response.json();

    var n = json.name;
    document.getElementById("city").innerHTML = n;

    const m = json.main;
    var t = m.temp;
    var h = m.humidity;
    var p = m.pressure;
    document.getElementById("temp").innerHTML = t + " °C";
    document.getElementById("hum").innerHTML = h + " %";
    document.getElementById("pres").innerHTML = p + " mPA";

    const w = json.weather;
    var d = w[0].description;
    document.getElementById("description").innerHTML = d;
}

// Preloader
(() => {
    window.addEventListener("load", function() {
        document.querySelector(".preloader").classList.add("opacity-0");
        setTimeout(function() {
            document.querySelector(".preloader").style.display = "none";
        }, 1000);
    });
})();
