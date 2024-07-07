//Exercise 1
    //1.1: alert: inside the funcOne function 3
    //1.2: TypeError: Assignment to constant variable.
    //2.1:
        // alert: inside the funcThree function 0
        // alert: inside the funcThree function 5
    //2.2: TypeError: Assignment to constant variable.
    //3.1: alert: inside the funcFive function hello
    //4: alert: inside the funcSix function test
    //4.2 same since it is redefined in the block
    //5: alert: in the if block 5
    //  alert: outside of the if block 2
    //5.2: same since it is redefined in the block

//Exercise 2
const winBattle = () => {
    return true;
}

let experiencePoints = winBattle() ? 10 : 1;

console.log(experiencePoints)

//Exercise 3

const isString = word => typeof(word) === "string"? true : false;
//Exercise 4

const getSum = (num1, num2) => num1 + num2;
//Exercise 5

function kgToGr(kg){
    return kg*1000
}

const kiloToGram = function(kg) {
    return kg*1000
};

// a function declaration is saved when the file is loaded, function expressions can be passed as arguments and can be anonymous

const kToG = (kg) => kg * 1000;
kToG(78)

//Exercise 6
((children, partner, location, title) => {
    p = document.createElement('p')
    p.innerText = `You will be a ${title} in ${location}, and married to ${partner} with ${children} kids.`
    document.body.appendChild(p)
})(4, 'Yona', 'Jerusalem', 'software engineer');
//Exercise 7
((username) => {
    const nav = document.getElementsByTagName('nav').item(0);
    const nameDiv = document.createElement('div');
    nameDiv.innerText = username;
    const profilePic = document.createElement('img');
    profilePic.setAttribute('src', 'https://images.ctfassets.net/h6goo9gw1hh6/2sNZtFAWOdP1lmQ33VwRN3/24e953b920a9cd0ff2e1d587742a2472/1-intro-photo-final.jpg?w=1200&h=992&q=70&fm=webp')
    nav.appendChild(nameDiv);
    nav.appendChild(profilePic)
})('MickJagger78');
//Exercise 8

function makeJuice(size){
    let ingredients = []
    function addIngredients(ing1, ing2, ing3){
        ingredients.push(ing1, ing2, ing3)
    }
    function displayJuice(){
        const p = document.createElement('p')
        p.innerText = `The client wants a ${size} juice, containing ${ing1}, ${ing2}, ${ing3}`;
    }
    addIngredients("apple", "banana", "orange");
    addIngredients("mango", "pineapple", "grape");
    displayJuice();
}

makeJuice('medium')

