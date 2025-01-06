import express from 'express'

const app = express()

app.get('/', (req, res) => {
  res.json({ status: 'OK' })
})

export default app
