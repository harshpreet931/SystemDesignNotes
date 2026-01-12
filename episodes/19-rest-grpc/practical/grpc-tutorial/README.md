# gRPC Tutorial Simple Greeting Service

A minimal gRPC example to understand the basics of Protocol Buffers and gRPC.

## What is gRPC?

gRPC is a high-performance RPC framework by Google that uses:
- **Protocol Buffers** - Binary serialization (faster than JSON)
- **HTTP/2** - Multiplexed streams
- **Contract-first** - Define your API in `.proto` files

## Quick Start

```bash
# Install dependencies
npm install

# Terminal 1: Start the server
npm run server

# Terminal 2: Run the client
npm run client Alice
# Output: Hello, Alice!

npm run client World
# Output: Hello, World!
```

## Files Explained

| File | Purpose |
|------|---------|
| `greeting.proto` | Defines the service and messages |
| `server.js` | Implements the gRPC server |
| `client.js` | Calls the gRPC service |

## The .proto File

```protobuf
syntax = "proto3";

package greeting;

service GreetingService {
  rpc SayHello (HelloRequest) returns (HelloReply) {}
}

message HelloRequest {
  string name = 1;
}

message HelloReply {
  string message = 1;
}
```

- **service**: Defines the RPC methods available
- **rpc**: An RPC method (endpoint)
- **message**: Structure of data being sent/received
- **= 1, = 2**: Field numbers (not values!)

## How It Works

```
┌──────────────┐                          ┌──────────────┐
│   Client     │      gRPC Call           │   Server     │
│  (client.js) │ ───────────────────────► │ (server.js)  │
│              │  {name: "Alice"}         │              │
│              │                          │  1. Load     │
│              │                          │     greeting.proto
│              │                          │              │
│              │  {message:               │  2. Call     │
│              │   "Hello, Alice!"}       │     sayHello()
│              │ ◄─────────────────────── │              │
└──────────────┘                          └──────────────┘
```

## Key Concepts

1. **Contract-First**: Define interface before coding
2. **Code Generation**: Protobuf compiler generates client/server stubs
3. **Type Safety**: Compiled languages get compile-time checking

## Next Steps

- Add more RPC methods (Server Streaming, Client Streaming)
- Try different field types (int32, bool, repeated)
- Explore gRPC with Go or Python