const amqp = require("amqplib");

async function recieveMessage() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  const exchange = "new_product_launch";

  await channel.assertExchange(exchange, "fanout", { durable: false });

  const queue = await channel.assertQueue("", { exclusive: false });
  console.log("Consumer2 waiting for messages : ", queue);

  await channel.bindQueue(queue.queue, exchange, "");

  channel.consume(queue.queue, (message) => {
    if (message) {
      console.log("Message received", JSON.parse(message.content));
      channel.ack(message);
    }
  });
}

recieveMessage();
