const apiKey = "248d369aa6322178f4f2620b2da7f29c";
let width;
let height;
function startApp()
{
    
    if(navigator.geolocation)
    {
        navigator.geolocation.getCurrentPosition(
            (position) => 
            {
                width = position.coords.latitude;
                height = position.coords.longitude;
                console.log(width,height);
                getWeatherData();
            }
        );
        
    }
}
function getWeatherData()
{
    
    let url = `https://api.openweathermap.org/data/2.5/weather?lat=${width}&lon=${height}&units=metric&appid=${apiKey}`;
    fetch(url)
    .then(response => response.json())
    .then(data => updateWeatherData(data))
}
function updateWeatherData(data)
{
    console.log(data);
    var slonce = data.sys;
    var wiatr = data.wind;

    var temp = data.main.temp;
    var pressure = data.main.pressure;
    var wilgotnosc = data.main.humidity;
    var wschod = new Date(slonce.sunrise*1000);//Funkcja konwertująca milisekundy na czas np:Tue May 04 2021 04:49:57 GMT+0200 (czas środkowoeuropejski letni)
    var zachod = new Date(slonce.sunset*1000);
    var speed = wiatr.speed;
    var zachmurzenie = data.clouds.all;
    var city = data.name;

    document.getElementById("miasto").innerHTML =city;
    document.getElementById("Temperatura").innerHTML=temp+"°C";
    document.getElementById("Wilgotność").innerHTML=wilgotnosc+"%";
    document.getElementById("Ciśnienie").innerHTML=pressure+"hPa";
    document.getElementById("Zachmurzenie").innerHTML =zachmurzenie+"%";
    document.getElementById("Szybkość wiatru").innerHTML=speed+"km/h";
    document.getElementById("Wschód słońca").innerHTML =wschod.getHours() + ":" +wschod.getMinutes();//tu wyodrebnia godz min
    document.getElementById("Zachód słońca").innerHTML =zachod.getHours() + ":" +zachod.getMinutes();
    
    let imgUrl = "http://openweathermap.org/img/wn/"+data.weather[0].icon+"@2x.png";
    document.getElementById("currentWeatherImg").setAttribute("src", imgUrl);
    
    const lokalizacja = document.getElementById("miasto");
    lokalizacja.href = `https://openstreetmap.org/#map=14/${width}/${height}`;
 
}

