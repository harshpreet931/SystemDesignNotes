# REST Tutorial Simple Greeting API

A minimal REST API example to understand the basics of HTTP APIs.

## What is REST?

REST (Representational State Transfer) is an architectural style that uses:
- **HTTP Methods**: GET, POST, PUT, DELETE
- **Resources**: Nouns (like `/users`, `/products`)
- **JSON**: Lightweight data format
- **Stateless**: Each request has all needed info

## Quick Start

```bash
# Install dependencies
npm install

# Start the server
npm start

# In another terminal, test with curl:
curl -X POST http://localhost:3000/greet \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice"}'
# Output: {"message":"Hello, Alice!"}

# Or run the client:
node client.js Alice
# Output: Hello, Alice!
```

## Files Explained

| File | Purpose |
|------|---------|
| `server.js` | Express server with `/greet` endpoint |
| `client.js` | Fetch client to call the API |

## The REST Pattern

```javascript
// POST creates a resource
app.post('/greet', (req, res) => {
  const name = req.body.name;
  res.json({ message: `Hello, ${name}!` });
});
```

- **POST**: Create/update resource
- **JSON**: Request/response format
- **Status Codes**: 200 (OK), 201 (Created), 404 (Not Found), etc.

## HTTP Methods

| Method | Action | Example |
|--------|--------|---------|
| GET | Retrieve | `GET /users` |
| POST | Create | `POST /users` |
| PUT | Replace | `PUT /users/1` |
| DELETE | Remove | `DELETE /users/1` |

## How It Works

```
┌──────────────┐    POST /greet     ┌──────────────┐
│   Client     │ ─────────────────► │   Server     │
│  (client.js) │  {name: "Alice"}   │ (server.js)  │
│              │                    │              │
│              │  {"message":       │  1. Parse    │
│              │   "Hello!"}        │     JSON body│
│              │ ◄───────────────── │  2. Process  │
└──────────────┘                    │  3. Respond  │
                                    └──────────────┘
```

## REST vs gRPC

| Aspect | REST | gRPC |
|--------|------|------|
| Format | JSON (text) | Protobuf (binary) |
| Protocol | HTTP/1.1 | HTTP/2 |
| Browsers | Native support | Needs proxy |
| Speed | Good | Faster |
| Learning | Easy | Medium |

## Next Steps

- Add GET endpoint: `app.get('/greet/:name', ...)`
- Add DELETE endpoint
- Add error handling: `res.status(404).json({error: "Not found"})`