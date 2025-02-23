const amqp = require("amqplib");

const queue = "message.queue";

async function recieveMessage() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertQueue(queue, { durable: false });

  console.log(`Waiting for messages in queue: ${queue}`);
  channel.consume(
    queue,
    (message) => {
      console.log("Received: ", message.content.toString());
    },
    { noAck: true }
  ); // delete message from queue
}

recieveMessage();
