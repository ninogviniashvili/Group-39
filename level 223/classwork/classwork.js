const fortunes = [
  'you will have a great day',
  'you will sleep',
  'surprise will come'
]

const argument = process.argv[2]

if (argument === 'start') {
  const randomFor = fortunes[Math.floor(Math.random() * fortunes.length)]

  const luckyNum = Math.floor(Math.random() * 100) + 1

  const randomYears = Math.floor(Math.random() * 90) + 1

  console.log("Fortune Teller Result:")
  console.log(`- your fortune: ${randomFor}`)
  console.log(`- lucky number: ${luckyNum}`)
  console.log(`- you will DIE at the age of : ${randomYears}`)
}