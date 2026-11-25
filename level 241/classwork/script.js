const http = require('http')

const handleGet = (req, res) => {
  const pathname = req.url

  if (pathname === '/') {
    res.end('Welcome to the Library')
  } else if (pathname === '/books') {
    res.end(JSON.stringify(['The Catcher in the Rye', 'Misery']))
  } else {
    res.statusCode = 404
    res.end('Not Found')
  }
}

const handlePost = (req, res) => {
  const pathname = req.url

  if (pathname === '/books') {
    res.end('New book added')
  } else {
    res.statusCode = 404
    res.end('Not Found')
  }
}

const handleDelete = (req, res) => {
  const pathname = req.url

  if (pathname === '/books') {
    res.end('Book deleted')
  } else {
    res.statusCode = 404
    res.end('Not Found')
  }
}

const server = http.createServer((req, res) => {
  const { method } = req

  switch (method) {
    case 'GET':
      return handleGet(req, res)
    case 'POST':
      return handlePost(req, res)
    case 'DELETE':
      return handleDelete(req, res)
  }
})

const PORT = 4001

server.listen(PORT, () => {
  console.log(`library server is running on http://localhost:${PORT}`)
})