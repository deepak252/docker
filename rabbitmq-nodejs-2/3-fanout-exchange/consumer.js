const amqp = require("amqplib");

const exchange = "logs.fanout";

async function recieveMessage() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertExchange(exchange, "fanout", { durable: false });
  const q = await channel.assertQueue("", { exclusive: true }); // The queue is deleted when the connection closes

  console.log(`Waiting for messages in queue: ${q.queue}`);

  await channel.bindQueue(q.queue, exchange, "");
  channel.consume(
    q.queue,
    (message) => {
      if (message?.content) {
        console.log("Received: ", message.content.toString());
      }
    },
    { noAck: true }
  ); // delete message from queue
}

recieveMessage();
