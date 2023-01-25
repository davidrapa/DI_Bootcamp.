function playTheGame() {
    let try3 = 3
    let ask1 = `asd`
    let confs = confirm(`want to play?`)
    let computerNumber = Math.floor(Math.random() * 11);
    if (!confs){
        alert (`No problem, Goodbye`)
    }else{
        while (isNaN(ask1) || ask1 < 0 || ask1 > 10){
            ask1 = prompt(`Enter a number between 0 and 10`)
        }
        let result = compareNumbers(ask1, computerNumber)
        console.log(result);
    } 
    if (ask1 > 10){
        alert(`Sorry its not a good number, Goodbye.`);
    } else {
    }

}

function compareNumbers(userNumber,computerNumber) {
    if (userNumber == computerNumber) {
        alert (`WINNER!!`)
        return true
    }else if (userNumber > computerNumber){
        alert (`Your number is bigger then the computers, guess again`)
        return false
    }else {
        alert (`Your number is smaller then the computer's, guess again`)
        return false
}
}






