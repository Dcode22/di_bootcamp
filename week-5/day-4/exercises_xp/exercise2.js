const form = document.querySelector('form');
console.log(form);
const fNameInput = document.getElementById('fname')
const lNameInput = document.getElementById('lname')
console.log(fNameInput)
console.log(lNameInput)
const submitBtn = document.getElementById('submit')
console.log(submitBtn)

console.log(document.getElementsByName('firstname')[0])
console.log(document.getElementsByName('lastname')[0])
const ul = document.querySelector('ul')
form.addEventListener('submit', event => {
    event.preventDefault();
    if(fNameInput.value && lNameInput.value){
        let li1 = document.createElement('li')
        li1.innerText = fNameInput.value;
        let li2 = document.createElement('li')
        li2.innerText = lNameInput.value;
        ul.appendChild(li1)
        ul.appendChild(li2)
    }
})