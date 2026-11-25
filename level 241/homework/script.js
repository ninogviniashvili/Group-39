const http = require('http')

const handleGetRequest = (req, res) => {
  const pathname = req.url

  if (pathname === '/menu') {
    res.end(JSON.stringify(['Espresso', 'Latte', 'Matcha']))
  } else if (pathname === '/hours') {
    res.end('Open from 8 AM to 8 PM')
  } else {
    res.end('Not Found')
  }
}

const handlePostRequest = (req, res) => {
  const pathname = req.url

  if (pathname === '/order') {
    res.end('Order received')
  } else {
    res.end('Not Found')
  }
}

const server = http.createServer((req, res) => {
  const { method } = req

  switch (method) {
    case 'GET':
      return handleGetRequest(req, res)
    case 'POST':
      return handlePostRequest(req, res)
    default:
      res.end('Method Not Allowed')
  }
})

server.listen(4001, () => {
  console.log('cafe menu server is running on http://localhost:4001')
})