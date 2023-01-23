// 🌟 Exercise 1 : Information
// Instructions


// Create a function called infoAboutMe() that takes no parameter.
// The function should console.log a sentence about you (ie. your name, age, hobbies ect…).
// Call the function.



// Part I : function with no parameters

// function infoAboutMe() {
//     console.log(`My name is David, i'm 38 years old, I like football`);
// }

// infoAboutMe()

// Part II : function with three parameters

// Create a function called infoAboutPerson(personName, personAge, personFavoriteColor) that takes 3 parameters.
// The function should console.log a sentence about the person (ie. “You name is …, you are .. years old, your favorite color is …”)
// Call the function twice with the following arguments:
// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

// function infoAboutPerson(personName, personAge, personFavoriteColor) {
//     console.log(`Your name is ${personName}, you are ${personAge}, your favorite colour is ${personFavoriteColor}`);
// }

// infoAboutPerson("David", 45, "blue")
// infoAboutPerson("Josh", 12, "yellow")

// 🌟 Exercise 2 : Tips
// Instructions
// John created a simple tip calculator to help calculate how much to tip when he and his family go to restaurants.

// Create a function named calculateTip() that takes no parameter.

// Inside the function, use prompt to ask John for the amount of the bill.

// Here are the rules
// If the bill is less than $50, tip 20%.
// If the bill is between $50 and $200, tip 15%.
// If the bill is more than $200, tip 10%.

// Console.log the tip amount and the final bill (bill + tip).

// // Call the calculateTip() function.

// function calculateTip() {
//     let askBill = prompt(`How much money did you spent?`)
//     if (askBill <= 50) {
// alert(`your bill is ${askBill} your tip is 20% ` +askBill*0.2)
//     }else if  (askBill >=51 && askBill <= 200) {
//         alert(`your bill is ${askBill} your tip is 15% ` +askBill*0.15)     
//     } else {
//         alert(`your bill is ${askBill} your tip is 10% ` +askBill*0.1)
//     }
// }

// calculateTip()

// 🌟 Exercise 3 : Find The Numbers Divisible By 23
// Instructions
// Create a function call isDivisible() that takes no parameter.

// In the function, loop through numbers 0 to 500.

// Console.log all the numbers divisible by 23.

// At the end, console.log the sum of all numbers that are divisible by 23.

// function isDivisible() {
// let asa = 0
// for (let i = 0 ; i < 500 ; i++){
// if(i%23 == 0 ){
//     console.log(i)
//     asa = asa +i
// }

// }

// isDivisible()

// 🌟 Exercise 4 : Shopping List
// Instructions

// Add the stock and prices objects to your js file.

// Create an array called shoppingList with the following items: “banana”, “orange”, and “apple”. It means that you have 1 banana, 1 orange and 1 apple in your cart.

// Create a function called myBill() that takes no parameters.

// The function should return the total price of your shoppingList. In order to do this you must follow these rules:
// The item must be in stock. (Hint : check out if .. in)
// If the item is in stock find out the price in the prices object.

// Call the myBill() function.

// Bonus: If the item is in stock, decrease the item’s stock by 1

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// let shoppingList = [`banana`, `orange`, `apple`]

// function myBill(){
//     let bill = 0;
//     for (let i of shoppingList){
//         if ( i in stock && stock[i] !== 0){
//             bill += prices[i];
//         }
//     }
// }
//     myBill()

// / 🌟 Exercise 6 : Vacations Costs
// Instructions
// Let’s create functions that calculate your vacation’s costs:

// Define a function called hotelCost().
// It should ask the user for the number of nights they would like to stay in the hotel.
// If the user doesn’t answer or if the answer is not a number, ask again.
// The hotel costs $140 per night. The function should return the total price of the hotel.

// Define a function called planeRideCost().
// It should ask the user for their destination.
// If the user doesn’t answer or if the answer is not a string, ask again.
// The function should return a different price depending on the location.
// “London”: 183$
// “Paris” : 220$
// All other destination : 300$

// Define a function called rentalCarCost().
// It should ask the user for the number of days they would like to rent the car.
// If the user doesn’t answer or if the answer is not a number, ask again.
// Calculate the cost to rent the car. The car costs $40 everyday.
// If the user rents a car for more than 10 days, they get a 5% discount.
// The function should return the total price of the car rental.

// Define a function called totalVacationCost() that returns the total cost of the user’s vacation by calling the 3 functions that you created above.
// Example : The car cost: $x, the hotel cost: $y, the plane tickets cost: $z.
// Hint: You have to call the functions hotelCost(), planeRideCost() and rentalCarCost() inside the function totalVacationCost().

// Call the function totalVacationCost()

    function hotelCost(){	
        let howManyNights = prompt('how many nights are you planning to stay?')
            if (howManyNights > 0){			
        }else {		
            alert('you need to input a number,refresh the page and try again.')
        }	
        return console.log(`great! it will be 140 $ per night so in total  for ${howManyNights} nights it will be ${howManyNights * 140} dollars`)}
    
        function planeRideCost(){	let flyTo = prompt('    where are you flying to?').toLowerCase()	
    if(flyTo === 'london'){		console.log(`great your flight to london will cost 183 $`)	} else if( flyTo === 'paris'){		console.log(`great your flight to paris will cost 220 $`)	}else if (flyTo !='paris' !='london') {		console.log(`your flight will cost 300$`)
                }}
    
    function rentalCarCost(){	let carDay = prompt('for how many days whold you like to rent a car?')	
    if (carDay > 0 && carDay <= 10) {		console.log(`great! your total is ${carDay * 40} dollars`)		}
    else if (carDay > 10) {		console.log(`great you get a discount so insted ${carDay * 40} your total is ${(carDay * 40) *0.95} dollars (5% off)`)			}else {		alert('refresh the page and insert a number!')	}
    }hotelCost(), planeRideCost(), rentalCarCost()
    
    let totalCost = function totalVacationCost(){
        alert(`your total for this vacation is a lot`)}
    totalCost()