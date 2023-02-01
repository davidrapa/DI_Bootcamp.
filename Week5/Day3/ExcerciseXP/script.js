
// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.
// function sayHello() {
//     alert(`Hello World`);
//   }
  
//   setTimeout(sayHello, 2000);

  // Part II
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.

function addP() {
    let getContainer = document.querySelector(`#container`);
    let p = document.createElement("p");
    let textNode = document.createTextNode("Hello World");
    p.appendChild(textNode);
    p.appendChild(getContainer)

  }
  
  setTimeout(addP, 2000);

//   / Part III
// In your Javascript file, using setInterval, call a function every 2 seconds.
// The function will add a new paragraph <p>Hello World</p> to the <div id="container">.
// The interval will be cleared (ie. clearInterval), when the user will click on the button.
// Instead of clicking on the button, the interval will be cleared (ie. clearInterval) as soon as there will be 5 paragraphs inside the <div id="container">.

// let timer = setInterval(myTimer, 2000);

// function myTimer() {
//     let getContainer = document.querySelector(`#container`);
//     let p = document.createElement("p");
//     let textNode = document.createTextNode("Hello World");
//     p.appendChild(textNode);
//     p.appendChild(getContainer)

// }

// function myStopFunction() {
//   clearInterval(timer);
// }

// let button = document.querySelector(`#clear`)
// button.addEventListener(`click`, myStopFunction)

// 🌟 Exercise 2 : Move The Box

// Copy the code above, to a structured HTML file.
// In your Javascript file, use setInterval to move the <div id="animate"> to the right side of the <div id="container">, when the button is clicked on.
// The <div id="animate"> should move 1px to the right every milisecond, until it reaches the end of the <div id="container">.
// Hint : use clearInterval as soon as the box reaches the right end side of the container
// Hint : check out the demonstration in the Course Noted named JS Functions

// let e = document.querySelector("#animate");
// var s = 1;
// setInterval(function(){
//     var eLeftPos = e.offsetLeft;
//     e.style.left = (eLeftPos + s) + 'px';

// }, 10);


// 🌟 Exercise 3: Drag & Drop
// Copy the code above, to a structured HTML file.
// In your Javascript file add the functionality which will allow you to drag the box and drop it into the target. Check out the Course Notes named DOM animations.

function allowDrop(ev) {
    ev.preventDefault();
  }
  
  function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
  }
  
  function drop(ev) {
    ev.preventDefault();
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
  }