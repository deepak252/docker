const amqp = require("amqplib");

// order notification service
async function receiveMessages() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  const exchange = "notification_exchange";
  const queue = "order_queue";
  await channel.assertExchange(exchange, "topic", { durable: false });
  await channel.assertQueue(queue, {durable: false});

  await channel.bindQueue(queue, exchange, 'order.*')

  channel.consume(queue, (message) => {
    if (message) {
      console.log("Order notification was consumed", JSON.parse(message.content));
      channel.ack(message); // Acknowledge that message has been received
    }
  });
}
receiveMessages();
