const express = require('express')
const app = express()
const bodyParser = require('body-parser')
const morgan = require('morgan')
const cors = require('cors')

const dataRouter = require('./controllers/data')
const sensorRouter = require('./controllers/sensor')

app.use(express.static('build'))
app.use(bodyParser.json())
app.use(cors())

morgan.token('body', (req, res) => JSON.stringify(req.body))
app.use(morgan(':method :url :body :status :res[content-length] - :response-time ms'))

app.use('/api/data',dataRouter)
app.use('/api/sensor',sensorRouter)

const PORT = process.env.PORT || 3001
app.listen(PORT, '0.0.0.0', () => {
  console.log(`Server listening on port ${PORT}`)
})

/*npm run watch*/