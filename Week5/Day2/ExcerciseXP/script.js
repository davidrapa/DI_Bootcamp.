// 🌟 Exercise 1 : Change The Article
// Instructions

// Using a DOM property, retrieve the h1 and console.log it.

// // Using DOM methods, remove the last paragraph in the <article> tag.

// // Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

// // Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

// // Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

// // BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

// // BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

// let h1 = document.querySelectorAll(`h1`)
// let removeP = document.getElementById(`remove`);
// removeP.remove();

// let h2click = document.querySelector(`.backgroundclick`)
// h2click.addEventListener("click", backgroundred);

// function backgroundred() { 
//     h2click.style.backgroundColor = "#ff0000"
// } 

// let h3click = document.querySelector(`.h3click`)
// h3click.addEventListener("click", displaynone);

// function displaynone() { 
//     document.querySelector(`.h3click`).style.display = "none";
// } 

// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

// let buttonBold = document.querySelector(`#clickbold`)
// buttonBold.addEventListener("click", displayBoldPtag);

// function displayBoldPtag() { 
// document.getElementsByTagName(p).style.fontWeight = `bold`
// } 

// 🌟 Exercise 2 : Work With Forms
// Instructions
// Copy the code below, into a structured HTML file:
// Retrieve the form and console.log it.

// Retrieve the inputs by their id and console.log them.

// Retrieve the inputs by their name attribute and console.log them.

// When the user submits the form (ie. submit event listener)
// use event.preventDefault(), why ?
// get the values of the input tags,
// make sure that they are not empty,
// create an li per input value,
// then append them to a the <ul class="usersAnswer"></ul>, below the form.

// let form1 = document.forms
// console.log(formName);

// let formName = document.getElementById(`#fname`)
// console.log(formName);

// console.log(document.forms.fname);
// console.log(document.forms.lname);

// let inputName = document.getElementById(`fname`)
// let inputLastName = document.getElementById(`lname`)
// let submitButton = document.querySelector(`#submit`)
// submitButton.addEventListener(`click`, getTags)


// function getTags() { 
// let li = document.createElement(`li`);
// li.appendChild(document.createTextNode(inputName.value))
// li.appendChild(document.createTextNode(inputLastName.value))
// ul.appendChild(li)
// } 

// 🌟 Exercise 3 : Transform The Sentence
// In the JS file:

// Declare a global variable named allBoldItems.

// Create a function called getBold_items() that takes no parameter. This function should collect all the bold items inside the paragraph and assign them to the allBoldItems variable.

// Create a function called highlight() that changes the color of all the bold text to blue.

// Create a function called return_normal() that changes the color of all the bold text back to black.

// Call the function highlight() on mouseover (ie. when the mouse pointer is moved onto the paragraph), and the function return_normal() on mouseout (ie. when the mouse pointer is moved out of the paragraph). Look at this example

// <p><strong>Hello</strong> I hope you are enjoying <strong>this</strong> class. At the
// <strong>end</strong> you <strong>will</strong> be great Developers!
// // <strong>Enjoy</strong> the <strong>JavaScript </strong> lessons</p>

// let allBoldItems = document.querySelectorAll(`strong`)

// function getBold_items() {
// document.querySelectorAll(`strong`)
// }
// function highlight() {
//     document.querySelectorAll(`strong`).style.color = "blue"
// }

// function return_normal() {
//     document.querySelectorAll(`strong`).style = null
// }

// allBoldItems.addEventListener("mouseover", highlight);
// allBoldItems.addEventListener("mouseout", return_normal);