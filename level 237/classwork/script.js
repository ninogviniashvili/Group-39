//1

const http = require('http')
const statusServer = http.createServer((req, res) => {
    res.end('Game server running')
})
statusServer.listen(5000)


//2

const apiUrl = 'https://api.gamehub.com/inventory/108/stats?view=detailed&format=json'
console.log(apiUrl)


//3
const URL_STRING = 'https://portal.net/reports/weekly?export=pdf&user=admin'
const parsedUrl = new URL(URL_STRING)
const domainName = parsedUrl.hostname
const resourcePath = parsedUrl.pathname
const queryParams = parsedUrl.searchParams
console.log(queryParams.get('export'))