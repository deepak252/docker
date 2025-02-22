const amqp = require("amqplib");

// payment notification service
async function receiveMessages() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  const exchange = "notification_exchange";
  const queue = "payment_queue";
  await channel.assertExchange(exchange, "topic", { durable: false });
  await channel.assertQueue(queue, {durable: false});

  await channel.bindQueue(queue, exchange, 'payment.*')

  channel.consume(queue, (message) => {
    if (message) {
      console.log("Payment notification was consumed", JSON.parse(message.content));
      channel.ack(message); // Acknowledge that message has been received
    }
  });
}
receiveMessages();
