//DOM Manipulation

let btn = document.getElementById("add-todo-btn");
let inputTodo = document.getElementById("input-todo");
let todosContainer = document.getElementById("todos-container");
let todosList = document.getElementById("todos-list");

// Adding Local storage for todos-list

function show() {
    let todosList = localStorage.getItem("todos-list");

    if (todosList == null) {
        todosObj = [];
    }   else {
        todosObj =JSON.parse(todosList);
    }
    localStorage.setItem("todosList", JSON.stringify(todosObj));

    let html = "";
    todosObj.forEach(function(key, value){
        html += `
        <li id="todo-${value}" class="todo">
            <div id="todo-text-container-${value}" class="todo-text-container">
             <input
              id="check-todo-btn-${value}"
              class="check-todo-btn"
              onclick="doneTodo(${value})"
              type="checkbox">
              <input
                id="todo-text-${value}"
                class="todo-text"
                readonly
                type="text"
                value="${key}">
            </div>
            <div
                id="btn-container-${value}"
                class="delete-todo-btn"
                onclick="doneTodo(${value})"
                type="checkbox">
              <input
                id="todo-text-${value}"
                class="todo-text"
                readonly
                type="text"
                value="${key}">
            </div>
            <div
              id="btn-container-${value}"
              class="btn-container">
              <button
                id="delete-todo-btn-${value}"
                class="delete-todo-btn"
                onclick="deleteTodo(${value})">
                <svg viewBox="0 0 448 512" width="20" height="20"  title="trash">
      <path d="M432 32H312l-9.4-18.7A24 24 0 0 0 281.1 0H166.8a23.72 23.72 0 0 0-21.4 13.3L136 32H16A16 16 0 0 0 0 48v32a16 16 0 0 0 16 16h416a16 16 0 0 0 16-16V48a16 16 0 0 0-16-16zM53.2 467a48 48 0 0 0 47.9 45h245.8a48 48 0 0 0 47.9-45L416 128H32z" />
    </svg>
              </button>
            <button
              id="edit-todo-btn-${value}"
              class="edit-todo-btn"
              onclick="editTodo(${value})">
              <svg viewBox="0 0 512 512" width="20" height="20" title="pencil-alt">
      <path d="M497.9 142.1l-46.1 46.1c-4.7 4.7-12.3 4.7-17 0l-111-111c-4.7-4.7-4.7-12.3 0-17l46.1-46.1c18.7-18.7 49.1-18.7 67.9 0l60.1 60.1c18.8 18.7 18.8 49.1 0 67.9zM284.2 99.8L21.6 362.4.4 483.9c-2.9 16.4 11.4 30.6 27.8 27.8l121.5-21.3 262.6-262.6c4.7-4.7 4.7-12.3 0-17l-111-111c-4.8-4.7-12.4-4.7-17.1 0zM124.1 339.9c-5.5-5.5-5.5-14.3 0-19.8l154-154c5.5-5.5 14.3-5.5 19.8 0s5.5 14.3 0 19.8l-154 154c-5.5 5.5-14.3 5.5-19.8 0zM88 424h48v36.3l-64.5 11.3-31.1-31.1L51.7 376H88v48z" />
    </svg>
            </button>
          </li>
        `
    });

    let todoElement = document.getElementById('todos-list');
if (todoObj.length != 0) {
    todoElement.innerHTML = html;
} else {
    todoElement
}


    const input-todo = [
        {
          Todo: 'Type a note',
          Text: 'Type a text'
        };
        {
        Todo: 'Type a note',
        Text: 'Type a text'
        };
        {
          Todo: 'Type a note',
          Text: 'Type a text'
        };
      ]
      
      localStorage.setItem('todosList', JSON.stringify('input-todo'));
      


};