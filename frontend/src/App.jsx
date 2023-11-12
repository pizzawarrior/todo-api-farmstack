import { useState, useEffect } from "react";
import "./App.css";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import TodoView from "./components/TodoListView";

function App() {
  const [todoList, setTodoList] = useState([{}])
  const [title, setTitle] = useState('')
  const [desc, setDesc] = useState('')

//   read all todos
useEffect(() => {
    axios.get('http://localhost:8000/api/todo')
        .then(res => {
            setTodoList(res.data)
    })
});

// post a todo
const addTodoHandler = () => {
    axios.post('http://localhost:8000/api/todo', { 'title':title,
    'description':desc })
        .then(res => console.log(res))
};



  return (
    <div
      className="App list-group-item justify-content-center align-items-center mx-auto"
      style={{ width: "400px", backgroundColor: "white", marginTop: "15px" }}
    >
      <h2
        className="card text-white bg-primary mb-1"
        stylename="max-width: 20rem;"
      >
        Task Manager
      </h2>
      <div className="card-body">
        <h5 className="card text-white bg-dark mb-3">Add a Task</h5>
        <span className="card-text">
          <input className="mb-2 form-control titleIn" onChange={e => setTitle(e.target.value)}
          placeholder="Title" />
          <input className="mb-2 form-control desIn" onChange={e => setDesc(e.target.value)}
            placeholder="Description"
          />
          <button
            className="btn btn-outline-primary mx-2 mb-3"
            style={{ borderRadius: "50px", fontWeight: "bold" }} onClick={addTodoHandler}
          >
            Add Task
          </button>
        </span>

        <h5 className="card text-white bg-dark mb-3">My Tasks</h5>

        <div>
            <TodoView todoList={todoList} />
        </div>
      </div>
    </div>
  );
}

export default App;
