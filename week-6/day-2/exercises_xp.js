//Exercise 1
const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
colors.forEach((color, i) => console.log(`#${i +1} choice is ${color}`))
if("Violet" in colors){
    console.log('yeah')
} else console.log('no')


//Exercise 2
const ordinal = ["th","st","nd","rd"];

colors.forEach((color, i) => {
    let ord = '';
    if(i > 2){
        ord = ordinal[0]
    } else ord = ordinal[i + 1]
    console.log(`${(i + 1) + ord} choice is ${color}`)
})


//Exercise 3
//1: ['bread', "carrot", "potato", 'chicken', "apple", "orange"]
//2: ['U', 'S', 'A']


//Exercise 4
const users = [{ firstName: 'Bradley', lastName: 'Bouley', role: 'Full Stack Resident' },
             { firstName: 'Chloe', lastName: 'Alnaji', role: 'Full Stack Resident' },
             { firstName: 'Jonathan', lastName: 'Baughn', role: 'Enterprise Instructor' },
             { firstName: 'Michael', lastName: 'Herman', role: 'Lead Instructor' },
             { firstName: 'Robert', lastName: 'Hajek', role: 'Full Stack Resident' },
             { firstName: 'Wes', lastName: 'Reid', role: 'Instructor'},
             { firstName: 'Zach', lastName: 'Klabunde', role: 'Instructor'}];

const welcomeStudents = users.map(user => `Welcome ${user.firstName}`)
const fullStackUsers = users.filter(user => user.role === 'Full Stack Resident')
console.log(welcomeStudents)
console.log(fullStackUsers)
//Exercise 5
const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
const epicString = epic.reduce((str = '', word) => str += word + " ")
console.log(epicString)

//Exercise 6

const students = [{name: "Ray", course: "Computer Science", isPassed: true}, 
               {name: "Liam", course: "Computer Science", isPassed: false}, 
               {name: "Jenner", course: "Information Technology", isPassed: true}, 
               {name: "Marco", course: "Robotics", isPassed: true}, 
               {name: "Kimberly", course: "Artificial Intelligence", isPassed: false}, 
               {name: "Jamie", course: "Big Data", isPassed: false}];

const passedStudents = students.filter(student => student.isPassed)
console.log(students)
console.log(passedStudents)