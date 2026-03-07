import React from 'react';
import { useState } from 'react';
import Presentational from './pres.jsx';


export default function Container() { 
    const [count, setCount] = useState(0);
  
    const increment = () => setCount(prev => prev + 1);
    const decrement = () => setCount(prev => prev - 1);
    const color = count > 0 ? 'green' : count < 0 ? 'red' : 'black'

  return (
    <>
    <Presentational count={count} onIncrement={increment} onDecrement={decrement} color={color} />
    </>
  )
}