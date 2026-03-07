import {useState} from 'react'
import React from 'react';


export default function Presentational({count, onIncrement, onDecrement, color}) { 
 return (
      <div style={{ textAlign: 'center', marginTop: '20px' }}>

      <h1 style={{color}}>{count}</h1>
      <button style={{ background: 'red', color: 'white'}} onClick={onIncrement}>Add</button>
      <button onClick={onDecrement}>Subtract</button>

    </div>
 )
}