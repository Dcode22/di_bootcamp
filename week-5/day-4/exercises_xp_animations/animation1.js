const cont = document.getElementById('container')
setTimeout(() => {
    alert("Hello World")
}, 2000)
setTimeout(() => {
    const newPar = document.createElement('p')
    newPar.innerText = "Hello World"
    cont.appendChild(newPar)
}, 2000)

const interval = setInterval(() => {
    const newPar = document.createElement('p')
    newPar.innerText = "Hello World"
    cont.appendChild(newPar)
    if(cont.childElementCount == 5){
        clearInterval(interval)
    }
}, 2000)

document.getElementById('clear').addEventListener('click', () => clearInterval(interval))