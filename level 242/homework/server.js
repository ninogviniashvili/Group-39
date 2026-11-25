const http = require("http")
const fs = require("fs")

// 1. რა მოხდება, თუ JSON.parse()-ის გარეშე ვეცდებით data.songs-ზე წვდომას?
// fs.readFile("utf8")-ით წაკითხული data არის სტრიქონი (string) და არა JS ობიექტი.
// JSON.parse()-ის გარეშე data.songs იქნება undefined (რადგან სტრიქონს .songs ფროფერთი არ აქვს).
//
// 2. რა როლს ასრულებს ჩვენი სერვერი იმ მომენტში, როცა ბაზიდან (playlist.json) მონაცემებს კითხულობს?
// ამ მომენტში სერვერი გამოდის როგორც მომხმარებელი მონაცემთა წყაროს სისტემის მიმართ -
// ის ითხოვს და იღებს მონაცემებს playlist.json-დან, ამუშავებს მათ და შემდეგ უკვე სერვერის როლში
// უბრუნებს პასუხს ბრაუზერს.

const server = http.createServer((req, res) => {
  if (req.method === "GET" && (req.url === "/random-song" || req.url === "/all-songs")) {
    fs.readFile("playlist.json", "utf8", (err, data) => {
      if (err) {
        res.writeHead(500, { "Content-Type": "text/plain; charset=utf-8" })
        res.end("Database error")
        return
      }

      const parsedData = JSON.parse(data)
      const songs = parsedData.songs

      res.writeHead(200, { "Content-Type": "application/json; charset=utf-8" })

      if (req.url === "/random-song") {
        const randomIndex = Math.floor(Math.random() * songs.length)
        const randomSong = songs[randomIndex]
        res.end(JSON.stringify(randomSong))
      } else if (req.url === "/all-songs") {
        res.end(JSON.stringify(songs))
      }
    })
  } else {
    res.writeHead(404, { "Content-Type": "text/plain; charset=utf-8" })
    res.end("Not found")
  }
})

server.listen(4000, () => {
  console.log("Server is running on http://localhost:4000")
})