const express = require('express');

const app = express()

// This is middleware
app.use(function(req, res, next) {
    console.log("This is middleware!")
    next();
})

app.get('/', (req, res) => {
  res.send('Hello World')
})

app.get('/health', function(req, res) {
    res.send("This route is running properly!")
})

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000')
})