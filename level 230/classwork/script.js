const movies = [
  { title: "Inception", genre: "Sci-Fi", rating: 8.8 },
  { title: "The Dark Knight", genre: "Action", rating: 9.0 },
  { title: "Spirited Away", genre: "Animation", rating: 8.6 },
  { title: "Pulp Fiction", genre: "Action", rating: 8.9 },
  { title: "Parasite", genre: "Thriller", rating: 7.5 }
]

function printMovie(movie) {
  console.log(`${movie.title} | ${movie.genre} | ${movie.rating}`)
}

function help() {
  console.log("genres: sci-fi, action, thriller, animation")
  console.log("all - show every movie")
  console.log("top - shows movies rated 9 or above")
  console.log("count - show total number of movies")
  console.log("best - show the highest-rated movie")
  console.log("low - show movies rated below 8")
  console.log("random - show a randomly selected movie")
  console.log("search <text> - search movies by title")
  console.log("rating <number> - show movies with at least that rating")
  console.log("help - show this menu")
  console.log("exit - makes you quit")
  console.log("Choose a command or genre: ")
}

help()

process.stdin.on("data", (input) => {
  const genre = input.toString().trim().toLowerCase()

  if (genre === "") {
    console.log("Please enter a genre or command")
    return
  }

  if (genre === "exit") {
    console.log("goodbye")
    process.exit()
  }

  if (genre === "help") {
    help()
    return
  }

  if (genre === "all") {
    for (const movie of movies) {
      printMovie(movie)
    }
    return
  }

  if (genre === "top") {
    for (const movie of movies) {
      if (movie.rating >= 9) {
        printMovie(movie)
      }
    }
    return
  }

  if (genre === "count") {
    console.log(`Total movies: ${movies.length}`)
    return
  }

  if (genre === "best") {
    let bestMovie = movies[0]
    for (const movie of movies) {
      if (movie.rating > bestMovie.rating) {
        bestMovie = movie
      }
    }
    printMovie(bestMovie)
    return
  }

  if (genre === "low") {
    for (const movie of movies) {
      if (movie.rating < 8) {
        printMovie(movie)
      }
    }
    return
  }

  if (genre === "random") {
    const randomIndex = Math.floor(Math.random() * movies.length)
    printMovie(movies[randomIndex])
    return
  }

  if (genre.startsWith("search ")) {
    const searchQuery = genre.replace("search ", "").trim()
    let searchCount = 0
    for (const movie of movies) {
      if (movie.title.toLowerCase().includes(searchQuery)) {
        printMovie(movie)
        searchCount++
      }
    }
    if (searchCount === 0) {
      console.log("No movies found matching that title.")
    }
    return
  }

  if (genre.startsWith("rating ")) {
    const ratingStr = genre.replace("rating ", "").trim()
    const ratingVal = Number(ratingStr)

    if (isNaN(ratingVal) || ratingVal < 0 || ratingVal > 10) {
      console.log("Error: Please enter a valid rating number between 0 and 10.")
      return
    }

    let ratingCount = 0
    for (const movie of movies) {
      if (movie.rating >= ratingVal) {
        printMovie(movie)
        ratingCount++
      }
    }
    if (ratingCount === 0) {
      console.log("No movies found with that rating or higher.")
    }
    return
  }

  let count = 0

  for (const movie of movies) {
    if (movie.genre.toLowerCase() === genre && movie.rating >= 8) {
      printMovie(movie)
      count++
    }
  }

  if (count === 0) {
    console.log("no movie found")
  } else {
    console.log(`found ${count} movies`)
  }
})