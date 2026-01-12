const name = process.argv[2] || 'World';

fetch('http://localhost:3000/greet', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name })
})
  .then(res => res.json())
  .then(data => console.log(data.message))
  .catch(err => console.error('Error:', err));