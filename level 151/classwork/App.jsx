import React, { useState } from "react";

function App() {
  const [count, setCount] = useState(0);

  function Increment() {
    if (count < 10) {
      setCount(count + 1);
    }
  }

  function Decrement() {
    if (count > -10) {
      setCount(count - 1);
    }
  }

  function Reset() {
    setCount(0);
  }

  let statusText = "";
  if (count > 0) {
    statusText = "Positive Number";
  } else if (count < 0) {
    statusText = "Negative Number";
  } else {
    statusText = "Zero";
  }

  return (
    <>
      <h1>{count}</h1>
      <p>{statusText}</p>

      <button onClick={Increment} disabled={count >= 10}>
        Increment
      </button>

      <button onClick={Decrement} disabled={count <= -10}>
        Decrement
      </button>

      <button onClick={Reset}>Reset</button>
    </>
  );
}

export default App;
