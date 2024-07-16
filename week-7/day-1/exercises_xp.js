//Exercise 1
function compareToTen(num){
    return new Promise((resolve, reject) => {
        if(num > 10){
            reject()
        } else resolve()
    } )
}

//Exercise 2

function fourSec(){
    return new Promise((res, rej) => {
        setTimeout(() => res('4 seconds passed'), 4000)
    })
}

fourSec().then(res => console.log(res))

//Exercise 3

const immediateResolve = new Promise(res => res(3))
const immediateReject = new Promise((res, rej) => rej('Boo!'))
immediateResolve.then(console.log)
immediateReject.catch(console.log)