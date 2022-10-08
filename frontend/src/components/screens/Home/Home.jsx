import React, { useState } from 'react'
import TodoItem from './item/TodoItem'
import CreateTodoField from './create-todo-field/CreateTodoField'
import axios from "axios"


const data = [
  {
    _id: 'd21dwsd',
    title: 'Finish the essay collaboration',
    isCompleted: false,
  },
  {
    _id: '2131fsaD',
    title: 'Read the next chapter of the book',
    isCompleted: false,
  },
  {
    _id: 'asdAD23jK',
    title: 'Send the finished assignment',
    isCompleted: false,
  },
]


  const Home = () => {
    const [dataU, setData] = React.useState({ nodes: [] });

    const fetchData = React.useCallback(async () => {
        const url = '/data';
        const result = await axios.get(url);

        setData({ nodes: result.data });
    }, []);

    React.useEffect(() => {
        fetchData();
    }, [fetchData]);

  console.log(dataU);

  const [todos, setTodos] = useState(data)

  const changeTodo = (id) => {
    const copy = [...todos]
    const current = copy.find(t => t._id === id)
    current.isCompleted = !current.isCompleted
    setTodos(copy)
  }

  const removeTodo = (id) => {
    setTodos([...todos].filter(t => t._id !== id))
  }

  return (
  <div className='text-white w-4/5 mx-auto'>
    <h1 className='text-2xl font-bold text-center mb-8'>Todo for junior</h1>
    {todos.map(todo => (<TodoItem key={todo._id} todo={todo} 
    changeTodo={changeTodo} removeTodo={removeTodo}/>))}
    <CreateTodoField setTodos={setTodos}/>
  </div>

  )
}

export default Home