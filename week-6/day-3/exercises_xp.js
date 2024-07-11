//Exercise 1
//I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

//Exercise 2
function displayStudentInfo(objUser){
    const {first, last} = objUser;
    return `Your full name is ${first} ${last}`
}

console.log(displayStudentInfo({first: 'Elie', last:'Schoppik'}));

//Exercise 3
const users = { user1: 18273, user2: 92833, user3: 90315 }
const array = Object.entries(users);
console.log(array)
const modArray = array.map(arr => [arr[0], arr[1] * 2])
console.log(modArray)
//Exercise 4
    //type is 'object'
//Exercise 5
    // 2
//Exercise 6
/* 
    1. false, false

    2.
        4
        4
        5
*/

class Animal {
    constructor(name, type, color){
        this.name = name;
        this.type = type;
        this.color = color;
    }
}

class Mamal extends Animal {
    constructor(name, type, color){
        super(name, type, color)
    }
    sound(snd){
        return `${snd}!!!! I'm a ${this.type} named ${this.name} and I'm ${this.color}.`
    }
}

const farmerCow = new Mamal('Betty', 'cow', 'black and white');
console.log(farmerCow.sound('MOOOO'));
