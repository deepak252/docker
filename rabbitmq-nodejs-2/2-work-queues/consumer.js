const amqp = require("amqplib");

const queue = "task.queue";

async function recieveMessage() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertQueue(queue, { durable: true });
  channel.prefetch(1)

  console.log(`Waiting for messages in queue: ${queue}`);
  channel.consume(
    queue,
    (message) => {
      const task = JSON.parse(message.content);
      console.log("Received: ", task.message);
      setTimeout(() => {
        console.log("Task done");
        channel.ack(message); // Manual acknowledgment
      }, task.sec * 1000);
    },
    { noAck: false } // Manual acknowledgment
  ); // delete message from queue
}

recieveMessage();
