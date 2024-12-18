const fetch = require('node-fetch');

const apiKey = 'f8378c48b30542d1244982c1f6049d4f';
const city = 'London';
const url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}`;

fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(`Weather in ${city}:`);
        console.log(`Temperature: ${data.main.temp}K`);
        console.log(`Weather: ${data.weather[0].description}`);
    })
    .catch(error => console.error('Error fetching weather data:', error));