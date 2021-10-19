// Selectors
const taskInput = document.getElementById('tasks')
const addButton = document.querySelector('.addbutton')
const taskList = document.querySelector('#list__task')
const saveContainer = document.querySelector('.save-container')
const filterOption = document.querySelector('#filter-todo')

// Eventlisteners
document.addEventListener('DOMContentLoaded', getTodos)
addButton.addEventListener('click', addTodo)
taskList.addEventListener('click', deleteTask)
taskList.addEventListener('click', editTask)
taskList.addEventListener('click', saveEdits)
filterOption.addEventListener('click', filterTodo)

// Functions

// Adding Task
function addTodo(e) {

  // Prevent reload
  e.preventDefault()
  // For tasks
  let element1 = document.createElement('div')
  element1.classList.add('.task-list')

  // Task template
  let taskTemplate = `<div
      class="task__lists d-flex align-items-center justify-content-around mb-3"
    >
      <div
        class="d-flex align-items-center justify-content-between w-75 mr-2"
        style="background-color: #fff"
      >
        <p class="list-group-item form-check">${taskInput.value}</p>
        <button type="button" class="btn completedbutton">
          <ion-icon name="checkmark-done-outline" class="complete-button"></ion-icon>
        </button>
      </div>
      <div class="d-flex buttoncontainer">
        <button type="button" class="btn btn-outline-success editbutton mr-1">
          <ion-icon name="create-outline" class="edit-button"></ion-icon>
        </button>
        <button type="button" class="btn btn-outline-danger deletebutton mr-1">
        <ion-icon name="trash-outline" class="delete-button"></ion-icon>
        </button>
      </div>
    </div>`
  // For tasks
  if (!taskInput.value) { window.alert('Hey there!! Add some task😉') }
  else {
    element1.innerHTML = taskTemplate
    taskList.appendChild(element1)

    // Add todo to local storage
    saveLocalTodos(taskInput.value)
  }

  // Clearing input
  taskInput.value = ""
}

// Deleting & Checking Task
function deleteTask(e) {
  const item = e.target

  // delete task
  if (item.classList[0] === "delete-button") {
    const todo = item.parentElement.parentElement.parentElement.parentElement
    removeLocalTodo(todo)
    todo.remove()
  } else if (item.classList[2] === 'deletebutton') {
    const todo = item.parentElement.parentElement.parentElement
    removeLocalTodo(todo)
    todo.remove()
  }

  // Check task
  if (item.classList[0] === "complete-button") {
    const todo = item.parentElement.parentElement.parentElement.parentElement
    todo.classList.toggle('completedtask')
  } else if (item.classList[1] === "completedbutton") {
    const todo = item.parentElement.parentElement.parentElement
    todo.classList.toggle('completedtask')
  }
}

// Editing task
function editTask(e) {
  const item = e.target
  const buttonContainer = document.querySelector(".buttoncontainer")
  // Edit task
  if (item.classList[0] === 'edit-button') {
    let ele = document.createElement('button')
    ele.classList.add('savebutton')
    ele.classList.add("btn,btn-outline-success")
    ele.innerHTML = `<button type="button" class="btn btn-outline-success mr-1">
          <ion-icon name="checkmark-done-outline" class="save-button"></ion-icon>
        </button>`
    buttonContainer.appendChild(ele)
    const todo = item.parentElement.parentElement.parentElement.childNodes[1].childNodes[1]
    todo.setAttribute('contenteditable', "true")
  }
}

// Save Editing
function saveEdits(e) {
  const item = e.target
  const buttonContainer = document.querySelector(".savebutton")
  //save edit
  if (item.classList[0] === "save-button") {
    const todo = item.parentElement.parentElement.parentElement.parentElement.parentElement.childNodes[0].childNodes[1].childNodes[1]
    todo.setAttribute('contenteditable', "false")
    buttonContainer.remove()
  }
}

// Filtering Todo
function filterTodo(e) {
  const todos = taskList.childNodes
  todos.forEach((todo) => {
    switch (e.target.value) {
      case 'All':
        todo.style.display = 'block'
        break;
      case 'Completed':
        if (todo.classList.contains('completedtask')) {
          todo.style.display = 'block'
        } else {
          todo.style.display = 'none'
        }
        break;
      case "Pending":
        if (!todo.classList.contains('completedtask')) {
          todo.style.display = 'block'
        } else {
          todo.style.display = 'none'
        }
        break;
    }
  })
}

// Save local Todos
function saveLocalTodos(todo) {
  // Check
  let todos
  if (localStorage.getItem('todos') === null) {
    todos = []
  } else {
    todos = JSON.parse(localStorage.getItem('todos'))
  }
  todos.push(todo)
  localStorage.setItem('todos', JSON.stringify(todos))
}


// Get todos
function getTodos() {
  // Check
  let todos
  if (localStorage.getItem('todos') === null) {
    todos = []
  } else {
    todos = JSON.parse(localStorage.getItem('todos'))
  }

  todos.forEach((todo) => {
    // For tasks
    let element1 = document.createElement('div')
    element1.classList.add('.task-list')

    // Task template
    let taskTemplate = `<div
      class="task__lists d-flex align-items-center justify-content-around mb-3"
    >
      <div
        class="d-flex align-items-center justify-content-between w-75 mr-2"
        style="background-color: #fff"
      >
        <p class="list-group-item form-check">${todo}</p>
        <button type="button" class="btn completedbutton">
          <ion-icon name="checkmark-done-outline" class="complete-button"></ion-icon>
        </button>
      </div>
      <div class="d-flex buttoncontainer">
        <button type="button" class="btn btn-outline-success editbutton mr-1">
          <ion-icon name="create-outline" class="edit-button"></ion-icon>
        </button>
        <button type="button" class="btn btn-outline-danger deletebutton mr-1">
        <ion-icon name="trash-outline" class="delete-button"></ion-icon>
        </button>
      </div>
    </div>`

    // For tasks
    element1.innerHTML = taskTemplate
    taskList.appendChild(element1)
  })
}

// Remove Todo
function removeLocalTodo(todo) {
  // Check
  let todos
  if (localStorage.getItem('todos') === null) {
    todos = []
  } else {
    todos = JSON.parse(localStorage.getItem('todos'))
  }
  const todoChildren = todo.children[0].children[0].children[0].innerHTML
  todos.splice(todos.indexOf(todoChildren), 1)
  localStorage.setItem('todos', JSON.stringify(todos))
}

