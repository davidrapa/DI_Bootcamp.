// Instructions
// In this exercise we will be creating a webpage with a black background as the universe and we will fill the universe with planets and their moons.
// We will provide the HTML page.
// You only have to work with a JS file.

// Create an array which value is the planets of the solar system.
// For each planet in the array, create a <div> using createElement. This div should have a class named "planet".
// Each planet should have a different background color. (Hint: you could add a new class to each planet - each class containing a different background-color).
// Finally append each div to the <section> in the HTML (presented below).
// Bonus: Do the same process to create the moons.
// Be careful, each planet has a certain amount of moons. How should you display them?
// Should you still use an array for the planets ? Or an array of objects ?

let planetSolarSystem = [`sun`, `mercury`, `venus`, `earth` ,`mars`, `pluto`]

let sun = document.createElement(`div`)
let textSun = document.createTextNode("Sun")
sun.appendChild(textSun)
sun.classList.add("planet")
sun.style.backgroundColor = `yellow`
sun.style.width = "300px";
sun.style.height = "300px";
document.querySelector(`.listPlanets`).appendChild(sun)

let mercury = document.createElement(`div`)
let textMercury = document.createTextNode("Mercury")
mercury.appendChild(textMercury)
mercury.classList.add("planet")
mercury.style.backgroundColor = `pink`
mercury.style.width = "50px";
mercury.style.height = "50px";
mercury.setAttribute(`id`,`mercury`);
document.querySelector(`.listPlanets`).appendChild(mercury)

let venus = document.createElement(`div`)
let textVenus = document.createTextNode("Venus")
venus.appendChild(textVenus)
venus.classList.add("planet")
venus.style.backgroundColor = `blue`
venus.style.width = "75px";
venus.style.height = "75px";
venus.setAttribute(`id`,`venus`);
document.querySelector(`.listPlanets`).appendChild(venus)

let earth = document.createElement(`div`)
let textEarth = document.createTextNode("Earth")
earth.appendChild(textEarth)
earth.classList.add("planet")
earth.style.backgroundColor = `#00ffff`
earth.setAttribute(`id`,`earth`);
document.querySelector(`.listPlanets`).appendChild(earth)

let mars = document.createElement(`div`)
let textMars = document.createTextNode("Mars")
mars.appendChild(textMars)
mars.classList.add("planet")
mars.style.backgroundColor = `#dc143c`
mars.style.width = "90px";
mars.style.height = "90px";
mars.setAttribute(`id`,`mars`);
document.querySelector(`.listPlanets`).appendChild(mars)

let pluto = document.createElement(`div`)
let textPluto = document.createTextNode("Pluto")
pluto.appendChild(textPluto)
pluto.classList.add("planet")
pluto.style.backgroundColor = `#dcdcdc`
pluto.style.width = "30px";
pluto.style.height = "30px";
pluto.setAttribute(`id`,`pluto`);
document.querySelector(`.listPlanets`).appendChild(pluto)

// Moons

let venusMoon = document.createElement("div")
let textVenusMoon = document.createTextNode("Moon Venus")
textVenusMoon.appendChild(textVenusMoon)
venusMoon.classList.add("moon")
let vMoon = document.getElementyById("venus");
vMoon.appendChild(venusMoon);