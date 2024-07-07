const tasks = [];

function addTask(event){
    event.preventDefault()
    let tasksContainer = document.getElementById('listTasks')
    let taskInput = document.getElementById('taskInput').value
    let toDoItemDiv = document.getElementsByClassName('to-do-item').item(0);
    let newTask = toDoItemDiv.cloneNode(true)
    newTask.querySelector('.to-do-text').innerText = taskInput;
    newTask.style.display = 'flex';
    tasksContainer.appendChild(newTask)
    tasks.push(taskInput)
}