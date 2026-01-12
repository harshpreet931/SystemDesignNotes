const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const proto = grpc.loadPackageDefinition(
  protoLoader.loadSync('greeting.proto')
).greeting;

function sayHello(call, callback) {
  callback(null, { message: `Hello, ${call.request.name}!` });
}

const server = new grpc.Server();
server.addService(proto.GreetingService.service, { SayHello: sayHello });
server.bindAsync('0.0.0.0:50051', grpc.ServerCredentials.createInsecure(), () => {
  console.log('gRPC Server running on port 50051');
});