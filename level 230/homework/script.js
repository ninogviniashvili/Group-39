const movies = [
  { title: "Inception", genre: "Sci-Fi", rating: 8.8, watched: false },
  { title: "The Dark Knight", genre: "Action", rating: 9.0, watched: false },
  { title: "Spirited Away", genre: "Animation", rating: 8.6, watched: false },
  { title: "Pulp Fiction", genre: "Action", rating: 8.9, watched: false },
  { title: "Parasite", genre: "Thriller", rating: 7.5, watched: false }
]

function printMovie(movie) {
  const status = movie.watched ? "Watched" : "Not watched"
  console.log(`${movie.title} | ${movie.genre} | ${movie.rating} | ${status}`)
}

function help() {
  console.log("genres: sci-fi, action, thriller, animation")
  console.log("all - show every movie")
  console.log("top - show movies rated 9 or above")
  console.log("help - show this menu")
  console.log("exit - quit")
  console.log("count - show the total number of movies")
  console.log("best - show the highest-rated movie")
  console.log("low - show movies rated below 8")
  console.log("random - show a random movie")
  console.log("search dark - search movie titles")
  console.log("rating 8.5 - show movies rated at least 8.5")
  console.log("watch <title> - mark a movie as watched")
  console.log("unwatch <title> - mark a movie as unwatched")
  console.log("watched - show watched movies")
  console.log("unwatched - show unwatched movies")
  console.log("suggest - recommend the highest-rated unwatched movie")
  console.log("Choose a command or genre:")
}

help()

process.stdin.on("data", (input) => {
  const genre = input.toString().trim().toLowerCase()

  if (genre === "") {
    console.log("Please enter a command or genre")
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
    const index = Math.floor(Math.random() * movies.length)
    printMovie(movies[index])
    return
  }

  if (genre === "watch" || genre.startsWith("watch ")) {
    const targetTitle = genre.slice(5).trim()

    if (targetTitle === "") {
      console.log("Please enter a movie title, for example: watch inception")
      return
    }

    let foundMovie = null

    for (const movie of movies) {
      if (movie.title.toLowerCase() === targetTitle) {
        foundMovie = movie
        break
      }
    }

    if (!foundMovie) {
      console.log(`Movie "${targetTitle}" not found`)
      return
    }

    if (foundMovie.watched) {
      console.log(`"${foundMovie.title}" is already watched`)
      return
    }

    foundMovie.watched = true
    console.log(`Marked "${foundMovie.title}" as watched`)
    return
  }

  if (genre === "unwatch" || genre.startsWith("unwatch ")) {
    const targetTitle = genre.slice(7).trim()

    if (targetTitle === "") {
      console.log("Please enter a movie title, for example: unwatch inception")
      return
    }

    let foundMovie = null

    for (const movie of movies) {
      if (movie.title.toLowerCase() === targetTitle) {
        foundMovie = movie
        break
      }
    }

    if (!foundMovie) {
      console.log(`Movie "${targetTitle}" not found`)
      return
    }

    if (!foundMovie.watched) {
      console.log(`"${foundMovie.title}" is already unwatched`)
      return;
    }

    foundMovie.watched = false
    console.log(`Marked "${foundMovie.title}" as unwatched`)
    return
  }

  if (genre === "watched") {
    let count = 0

    for (const movie of movies) {
      if (movie.watched) {
        printMovie(movie)
        count++
      }
    }

    if (count === 0) {
      console.log("No watched movies found")
    } else {
      console.log(`Found ${count} watched movies`)
    }

    return
  }

  if (genre === "unwatched") {
    let count = 0

    for (const movie of movies) {
      if (!movie.watched) {
        printMovie(movie)
        count++
      }
    }

    if (count === 0) {
      console.log("No unwatched movies found")
    } else {
      console.log(`Found ${count} unwatched movies`)
    }

    return
  }

  if (genre === "suggest") {
    let bestUnwatched = null

    for (const movie of movies) {
      if (!movie.watched) {
        if (bestUnwatched === null || movie.rating > bestUnwatched.rating) {
          bestUnwatched = movie
        }
      }
    }

    if (!bestUnwatched) {
      console.log("You have watched every movie! No new suggestions right now.")
      return
    }

    console.log("Recommended movie:");
    printMovie(bestUnwatched)
    return
  }

  if (genre === "search" || genre.startsWith("search ")) {
    const searchText = genre.slice(6).trim()

    if (searchText === "") {
      console.log("Enter a title to search, for example: search dark")
      return
    }

    let count = 0

    for (const movie of movies) {
      if (movie.title.toLowerCase().includes(searchText)) {
        printMovie(movie)
        count++
      }
    }

    if (count === 0) {
      console.log("No matching titles found")
    } else {
      console.log(`Found ${count} movies`)
    }

    return
  }

  if (genre === "rating" || genre.startsWith("rating ")) {
    const ratingText = genre.slice(6).trim()
    const minimumRating = Number(ratingText)

    if (
      ratingText === "" ||
      !Number.isFinite(minimumRating) ||
      minimumRating < 0 ||
      minimumRating > 10
    ) {
      console.log("Please enter a rating between 0 and 10")
      return
    }

    let count = 0

    for (const movie of movies) {
      if (movie.rating >= minimumRating) {
        printMovie(movie)
        count++
      }
    }

    if (count === 0) {
      console.log("No movies match that rating")
    } else {
      console.log(`Found ${count} movies`)
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