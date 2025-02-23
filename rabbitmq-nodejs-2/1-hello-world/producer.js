const amqp = require("amqplib");

const queue = "message.queue";
const message = "Hello World";

async function sendMessage() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertQueue(queue, { durable: false });

  channel.sendToQueue(queue, Buffer.from(message));
  console.log("Sent: ", message);

  setTimeout(() => {
    connection.close();
    process.exit(0);
  }, 500);
}

sendMessage();