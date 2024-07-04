let currentColor = '';
const colorSquares = document.querySelectorAll('#sidegrid > div')
const drawingSquares = document.querySelectorAll('#drawing-board > div')
document.getElementById('clearBtn').addEventListener('click', clear)
function clear(clearBtn = false){
    console.log('clear: ', clearBtn)
    colorSquares.forEach(color => {
        color.style.border = '1px solid black';
    })
    if(clearBtn){
        currentColor = '';
        drawingSquares.forEach(square => {
            square.style.backgroundColor = 'white';
        })
    }
}

colorSquares.forEach(color => color.addEventListener('click', () => {
    clear()
    currentColor = color.computedStyleMap().get('background-color').toString();
    console.log('currentColor: ', currentColor);
    color.style.border = '3px solid blue';
}))
let isMouseDown = false;
document.getElementById('drawing-board').addEventListener('mousedown', () => isMouseDown = true)
document.getElementById('drawing-board').addEventListener('mouseup', () => isMouseDown = false)
drawingSquares.forEach(square => {
    square.addEventListener('mouseover', () => {
        if(isMouseDown){
            square.style.backgroundColor = currentColor;
        }
    })
})





