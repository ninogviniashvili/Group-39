const http = require('http')

// 1
const myServer = http.createServer((req, res) => {
  res.end('Welcome to my server!')
})

myServer.listen(4000, () => {
  console.log('Server is running')
})


// 2
const basep = 'https://api.streamhub.com/creators'
const target = `${basep}/77/videos`

console.log('Target URL:', target)


// 3
const final = `${target}?filter=trending&limit=10`

console.log('Final URL:', final)


// 4
const portalUrl = 'https://developer.mozilla.org/en-US/docs/Web/HTTP?version=2&lang=en'
const urlObj = new URL(portalUrl)

console.log('Hostname:', urlObj.hostname)
console.log('Pathname:', urlObj.pathname)


// 5
const version = urlObj.searchParams.get('version')
const lang = urlObj.searchParams.get('lang')

console.log('Exercise 5 - Version:', version)
console.log('Exercise 5 - Lang:', lang)