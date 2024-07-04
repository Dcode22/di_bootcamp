let allBoldItems = [];
function getBoldItems(){
    allBoldItems = document.querySelectorAll('strong')  
}
getBoldItems();

function highlight(){
    allBoldItems.forEach(item => item.style.color = 'blue')
}

function returnItemsToDefault(){
    allBoldItems.forEach(item => item.style.color = 'inherit')
}

const paragraph = document.querySelector('p');
paragraph.addEventListener('mouseover', highlight)
paragraph.addEventListener('mouseout', returnItemsToDefault)