// 🌟 Exercise 1 : Users
// Instructions
// <div id="container">Users:</div>
// <ul class="list">
//     <li>John</li>
//     <li>Pete</li>
// </ul>
// <ul class="list">
//     <li>David</li>
//     <li>Sarah</li>
//     <li>Dan</li>
// </ul>
// Add the code above, to your HTML file
// Using Javascript:
// Retrieve the div and console.log it
// Change the name “Pete” to “Richard”.
// Change each first name of the two <ul>'s to your name.
// Delete the <li> that contains the text node “Sarah”.

// Bonus - Using Javascript:
// Add a class called student_list to both of the <ul>'s.
// Add the classes university and attendance to the first <ul>.

// let div = document.querySelector(`#container`)
// console.log(div);

// let pete = document.querySelector(`#change`)
// pete.textContent = "richars";
// console.log(pete);

// let changeName = document.getElementsByTagName("ul")[0]
// changeName.textContent= (`David1`)

// // let list = document.querySelector(".delSarah")
// // list.innerHTML = "";

// let element = document.getElementsByClassName("list");
// element.classList.add("student_list");


// Instructions
// <div>Users:</div>
// <ul>
//     <li>John</li>
//     <li>Pete</li>
// </ul>

// Add the code above, to your HTML file

// Add a “light blue” background color and some padding to the <div>.

// Do not display the <li> that contains the text node “John”.

// Add a border to the <li> that contains the text node “Pete”.

// Change the font size of the whole body.

// Bonus: If the background color of the div is “light blue”, alert “Hello x and y” (x and y are the users in the div).

// let divBackground = document.querySelector("#color").style.background = "blue";
// // divBackground.style.padding = `25px 50px 75px 100px`

// // document.getElementById("nodisplay").style.display = "none";

// document.getElementById(`addborder`).style.border = `solid red`

// document.body.style.fontSize = "x-large";

// if (document.querySelector("#color").style.background == "blue") {
//     alert (`Hello ${document.getElementById(`nodisplay`).textContent} and ${document.getElementById(`addborder`).textContent}`)
// }

// 🌟 Exercise 3 : Change The Navbar
// Instructions
// {/* <div id="navBar">
//     <ul>
//         <li><a href="#">Profile</a></li>
//         <li><a href="#">Home</a></li>
//         <li><a href="#">My Friends</a></li>
//         <li><a href="#">Messenger</a></li>
//         <li><a href="#">My Pics</a></li>
//     </ul>
// </div> */}
// // Add the code above, to your HTML file

// In the <div>, change the value of the id attribute from navBar to socialNetworkNavigation, using the setAttribute method.

// We are going to add a new <li> to the <ul>.
// First, create a new <li> tag (use the createElement method).
// // Create a new text node with “Logout” as its specified text.
// // Append the text node to the newly created list node (<li>).
// // Finally, append this updated list node to the unordered list (<ul>), using the appendChild method.

// // Bonus
// // Use the firstElementChild and the lastElementChild properties to retrieve the first and last <li> elements from their parent element (<ul>). Display the text of each link. (Hint: use the textContent property).


// let changeIdNavBar = document.getElementById('navBar').setAttribute('id', 'socialNetworkNavigation');
// console.log(changeIdNavBar);

// let createLiTag = document.createElement("li");
// let textli = document.createTextNode("Logout");
// createLiTag.appendChild(textli)

// document.getElementById("navlist").appendChild(createLiTag);

// console.log(document.getElementById(`navlist`).firstElementChild.textContent);
// console.log(document.getElementById(`navlist`).lastElementChild.textContent);
