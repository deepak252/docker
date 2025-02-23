const amqp = require("amqplib");

const queue = "logs.queue";
const exchange = "logs.fanout";
const message = "Hello World";

async function sendMessage() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertExchange(exchange, 'fanout', { durable: false });

  channel.publish(exchange, '', Buffer.from(message))
  setTimeout(() => {
    connection.close();
    process.exit(0);
  }, 500);
}

sendMessage();
