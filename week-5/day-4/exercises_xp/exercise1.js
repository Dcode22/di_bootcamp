let h1 = document.querySelector('h1');
console.log(h1);

let lastParagraph = document.querySelector('article p:last-of-type');
lastParagraph.remove();

let h2 = document.querySelector('h2');
h2.addEventListener('click', () => h2.style.color = 'red');

let h3 = document.querySelector('h3');
h3.addEventListener('click', () => h3.style.display = 'none');

let button = document.createElement('button')
document.body.appendChild(button);
button.innerText = 'Bold';
button.addEventListener('click', () => {
    document.querySelectorAll('p').forEach(element => {
        element.style.fontWeight = 'bold';
    });
});
