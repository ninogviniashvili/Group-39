const http = require('http')
const fs = require('fs')

const server = http.createServer((req, res) => {
  if (req.url === '/random-agent' && req.method === 'GET') {
    fs.readFile('./agents.json', 'utf-8', (err, data) => {
      if (err) {
        res.statusCode = 500
        return res.end('Database error')
      }

      const parsedData = JSON.parse(data)
      const agentsList = parsedData.agents
      const randomIndex = Math.floor(Math.random() * agentsList.length)
      const randomAgent = agentsList[randomIndex]

      res.statusCode = 200
      res.end(JSON.stringify(randomAgent))
    })
  } else {
    res.statusCode = 404
    res.end('Route not found')
  }
})

server.listen(3000, () => {
  console.log('Server is running on http://localhost:3000/random-agent')
})