// import React, { useEffect, useState } from 'react';
// import './App.css';

// export default function App() {
//   const [movie, setMovie] = useState("");
//   const [data, setData] = useState(null);

//   const handleSearch = () => {
//     if (!movie) return;

//     fetch(`https://api.themoviedb.org/3/search/movie?api_key=07d3978b5882d68e296023f77ae46c95&query=${encodeURIComponent(movie)}`)
//       .then((res) => res.json())
//       .then((json) => setData(json.results[0]));

//     console.log(data);
//   };

//   useEffect(() => {
//     if (movie) handleSearch();
//   }, [movie]);

//   const standardizePopularity = (val) => {
//     if (!val) return 0;
//     const score = Math.log10(val + 1) * 20;
//     return Math.min(Math.round(score), 100);
//   };

//   return (
//     <div className='bg-[#000309] h-screen relative overflow-hidden'>
//       {/* Backdrop Image Layer */}
//       {data?.backdrop_path && (
//         <div 
//           className="absolute inset-0 z-0 opacity-40"
//           style={{
//             backgroundImage: `url(https://image.tmdb.org/t/p/original${data.backdrop_path})`,
//             backgroundSize: 'cover',
//             backgroundPosition: 'center',
//           }}
//         />
//       )}

//       {/* Content Layer (z-10 ensures it stays above the backdrop) */}
//       <div className="relative z-10 flex flex-col justify-center items-center">
//         <div className='flex justify-center items-center h-60 gap-5'>
//           <input
//             className='border border-black text-black rounded-[15px] p-2 w-100 bg-[#d9d9d9]'
//             type="text"
//             placeholder='Enter a Movie..'
//             value={movie}
//             onChange={(e) => setMovie(e.target.value)}
//           />
//           <button onClick={handleSearch} className='bg-[#d9d9d9] text-black p-2 rounded-[15px]'>
//             Search
//           </button>
//         </div>

//         {/* results section*/}
//         {data && (
//           <div className='flex justify-center items-center gap-5 bg-[#2c2c2c] w-140 rounded-lg '>
//             <div>
//               <img
//                 className='rounded-lg'
//                 src={"https://image.tmdb.org/t/p/w300" + data?.poster_path}
//                 alt="poster"
//               />
//             </div>

//             <div className='flex w-60 flex-col gap-3 mr-5'>
//               <h1 className='text-white text-2xl'>{data.title}</h1>
//               <p className='text-white text-sm'>{data.overview}</p>
//               <button className='bg-white p-1 rounded-lg w-20'>
//                 {data.vote_average?.toFixed(1)} IMDB
//               </button>
//             </div>
//           </div>
//         )}
//       </div>
//     </div>
//   );
// }