import React from 'react'

function App(props) {
  return <h1>{props.name}</h1>
}
export default App



// function App() {
//   return <h1>hi</h1>
// }

// 1. შექმენით კომპონენტი, სადაც გექნებათ სია ელემენტებით (სტრინგებით),
//  შემდეგ ამ სიას გადაუარეთ map() ფუნქციით და თითოეული ელემენტის მეშვეობით 
// შექმენით p (რომელსაც შიგთავსად, textContent-ად, ექნება სტრინგი)

// function App() { 
//   const items = ['one', 'two', 'three', 'four']
  
//   return (  
//     <div>
//       {items.map((item, index) => (
//         <p key={index}>{item}</p>
//       ))}
//     </div>
//   )
// }

// 1. შექმენით კომპონენტი (props პარამეტრით) რომელსაც დააექსპორტებთ და დააიმპორტებთ მეორე კომპონენტში და იქიდან გადასცემთ props-ებს, რათქმაუნდა მთავარ ფაილში ეს მეორე კომპონენტი უნდა გქონდეთ დარენდერებული

// 1. შექმენით კომპონენტი, მას props-ებად გადაეცით რამდენიმე მნიშვნელობა, შემდეგ ეს მნიშვნელობები გამოიყენეთ კომპონენტშივე.

// 2. შექმენით კომპონენტი და შიგნით გქონდეთ event handler, return-ში არსებულ ღილაკზე დაჭერისას გაეშვას მაგალითად.

// function App(props) {
//   const handleClick = () => {
//     alert(`Hello, ${props.name}!`);
//   };
  
//   return (
//     <div>
//       <h1>{props.name}</h1>
//       <button onClick={handleClick}>Click Me</button>
//     </div>
//   );
// }
// export default App;

