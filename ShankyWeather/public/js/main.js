const cityName = document.getElementById("cityName");
const city_name = document.getElementById("city_name");
const submitBtn=document.getElementById("submitBtn");
const temp_status = document.getElementById("temp_status");
const temp_real = document.getElementById("temp_real");
const datahide = document.querySelector(".middle_layer");

const getInfo = async(event)=>{
    event.preventDefault();
    let cityVal = cityName.value;
    if(cityVal==""){
         city_name.innerHTML="<h2 style='font-size:2rem; font-weight:600; font-style:italic;'>*Please enter the  name of the city.</h2>"
         datahide.classList.add('data_hide');
        }
        else{
            try{
                let url = `https://api.openweathermap.org/data/2.5/weather?q=${cityVal}&units=metric&appid=e692ce7c4e9a52ddace8478bc182cec3` 
                const response = await fetch(url);
                const data = await response.json();
                const arrData = [data];
                
                temp_real.innerText = arrData[0].main.temp;
                city_name.innerText=`${arrData[0].name}, ${arrData[0].sys.country}`;
                const tempMood = arrData[0].weather[0].main;
                
                if(tempMood=="Clear"){
                    temp_status.innerHTML=
                    "<i  class='fas fa-sun' style='color:#ecca68'></i>"
                } else if(tempMood=="Clouds"){
                    temp_status.innerHTML=
                    "<i  class='fas fa-cloud' style='color:#f1f2f6'></i>"
                } else if(tempMood=="Rain"){
                    temp_status.innerHTML=
                    "<i  class='fas fa-cloud-rain' style='color:#477498'></i>"
                } else {
                    temp_status.innerHTML=
                    "<i  class='fas fa-cloud' style='color:#f1f2f6'></i>"
                }
                datahide.classList.remove('data_hide');
                
            }catch{
                city_name.innerHTML="<h2 style='font-size:2rem; font-weight:600; font-style:italic;'>*Please enter a valid city name.</h2>"
                datahide.classList.add('data_hide');
            
        }  
        }
}
submitBtn.addEventListener('click',getInfo);