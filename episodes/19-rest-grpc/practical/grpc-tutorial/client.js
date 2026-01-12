const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');

const proto = grpc.loadPackageDefinition(
  protoLoader.loadSync('greeting.proto')
).greeting;

const client = new proto.GreetingService(
  'localhost:50051',
  grpc.credentials.createInsecure()
);

client.SayHello({ name: process.argv[2] || 'World' }, (err, response) => {
  if (err) {
    console.error('Error:', err);
    return;
  }
  console.log(response.message);
});