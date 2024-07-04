const animateDiv = document.getElementById('animate')
const containerDiv = document.getElementById('container')
function myMove(){
    let left = 0
    const interval = setInterval(() => {
        animateDiv.style.left = left + 1 + 'px'
        if(left == 350){
            clearInterval(interval)
        }
        left = left + 1;
    }, 1)
}