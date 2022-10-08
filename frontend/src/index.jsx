import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Graph from './components/screens/Home/item/Graph';
import LayoutU from './components/layout/LayoutU';
import Counter from './components/screens/Home/item/Counter';
import Table from './components/screens/Home/item/Table';




const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <LayoutU graph={<Graph />} counter={<Counter />} table={<Table />} />
      {/* <Graph />
      <Counter />
      <Table /> */}
    {/* </LayoutU> */}
  </React.StrictMode>
)
