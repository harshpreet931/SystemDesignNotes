const express = require('express');
const app = express();

app.use(express.json());

app.post('/greet', (req, res) => {
  const name = req.body.name;
  res.json({ message: `Hello, ${name}!` });
});

app.listen(3000, () => {
  console.log('REST Server running on port 3000');
});