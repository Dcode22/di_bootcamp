//Exercise 1
function displayNumbersDivisible(){
    let total = 0
    for(let i = 1; i <= 500; i++){
        if(i%23 == 0){
            total+=i;
            console.log(i)
        }
    }
    console.log('total: ', total)
}

displayNumbersDivisible()

//Exercise 2
const stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

const prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

let shoppingList = ['banana', 'orange', 'apple']

function myBill(){
    let total = 0;
    shoppingList.forEach(item => {
        if(stock[`${item}`] > 0){
            total += prices[`${item}`]
        }
    })
    return total;
}

console.log(myBill())

//Exercise 3

const changeEnough = (itemPrice, amountOfChange) => {
    let total = 0
    let denomintations = [0.25, 0.10, 0.05, 0.01]
    for(let i = 0; i < amountOfChange.length; i++) {
        total += (amountOfChange[i] * denomintations[i]);
    }
    console.log('total: ', total)
    if(total >= itemPrice){
        return true
    } else return false
}

console.log(changeEnough(2.5, [10, 2, 3, 1]))

//Exercise 4

function hotelCost(){
    let numberOfNights = parseInt(prompt('How many nights would you like to book? '))
    if(isNaN(numberOfNights)){
        hotelCost()
    }
    return 140 * numberOfNights
}

function planeRideCost(){
    let destination = prompt('Enter your destination: ')
    let price = 300;
    if(!destination || typeof(destination) != "string"){
        planeRideCost()
    }
    if(destination.toLowerCase() == 'london'){
        price = 183
    } else if(destination.toLowerCase() == 'paris'){
        price = 220
    }
    return price
}


function rentalCarCost(){
    let numDays = prompt('How many days would you like to rent?')
    if(!numDays || isNaN(numDays)){
        rentalCarCost()
    }
    let price = numDays * 40;
    if(numDays > 10){
        price = price * 0.95;
    }
    return price;
}

function totalVacationCost(){
    return hotelCost() + planeRideCost() + rentalCarCost()
}

totalVacationCost()

//Exercise 5
// see ./exercise5.html

//Exercise 6
