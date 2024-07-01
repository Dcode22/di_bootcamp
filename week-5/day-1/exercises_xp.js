// Exercise 1
const people = ["Greg", "Mary", "Devon", "James"];

people.shift()
people.pop()
people.push('Jason')
people.push('Dave')
console.log(people)
console.log(people.indexOf('Mary'))
people_copy = people.slice(1, -1)
console.log(people_copy)
console.log(people.indexOf('Foo'))
let last = people[people.length - 1]
console.log(last)

for (person of people){
    console.log(person)
}

for (person of people){
    console.log(person)
    if(person == 'Devon'){
        break
    }
}

//Exercise 2
let colors = ['blue', 'yellow', 'red', 'black', 'white']
let suffixes = ['st', 'nd', 'rd', 'th', 'th']
for(let i = 0; i < colors.length; i++){
    console.log(`My ${(i+1) + suffixes[i]} choice is ${colors[i]}`)
}

// Exercise 3 
let userNumber;
do {
    userNumber = parseInt(prompt('Enter a number:'));
    console.log(typeof(userNumber));
} while (userNumber < 10);

// Exercise 4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building.numberOfFloors)
console.log(building.numberOfAptByFloor.firstFloor, building.numberOfAptByFloor.thirdFloor)
console.log(building.nameOfTenants[1], building.numberOfRoomsAndRent.dan[0])
if(building.numberOfRoomsAndRent.sarah[1] + building.numberOfRoomsAndRent.david[1] > building.numberOfRoomsAndRent.dan[1]){
    building.numberOfRoomsAndRent.dan[1] = 1200
}

//Exercise 5
let family = {
    dad: 'Dave',
    mom: 'Sara',
    kid1: 'Joey',
    kid2: 'Vivy'
}
for(key in family){
    console.log(key)
}
for(key in family){
    console.log(family[key])
}

//Exercise 6 
const details = {
    my: 'name',
    is: 'Rudolf',
    the: 'reindeer'
}


statement = ""
Object.entries(details).forEach(([key, value]) => {
    statement += key + ' ';
    statement += value + ' ';
})
console.log(statement)

// Exercise 7 
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
names.sort()
let secretName = '';
names.forEach(name => {
    secretName += name[0].toUpperCase();
})
console.log(secretName)
