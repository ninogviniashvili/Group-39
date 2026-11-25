// const http = require('http')

// const lobbyServer = http.createServer((req, res) => {
//     res.end('matchmaking lobby ready. waiting for players...')
// })

// lobbyServer.listen(7000)


const mediaUrl = 'https://telemetry.gamingservers.net/metrics/v2?region=eu-central&ping=42& tickrate=128'

const streamDetails = new URL(mediaUrl)

const platformHost = streamDetails.hostname

const streamPath = streamDetails.pathname

const title = streamDetails.searchParams.get('title')

const resolution = streamDetails.searchParams.get('resolution')

console.log(title)
console.log(resolution)