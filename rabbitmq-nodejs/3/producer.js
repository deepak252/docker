const amqp = require("amqplib");

async function sendMessage(routingKey, message) {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  const exchange = "notification_exchange";
  await channel.assertExchange(exchange, "topic", { durable: false });

  channel.publish(exchange, routingKey, Buffer.from(JSON.stringify(message)));

  console.log("Message sent - ", { routingKey }, { message });

  setTimeout(() => {
    connection.close();
  }, 500);
}

sendMessage("order.placed", {orderId: '1234', status: 'placed'})
sendMessage("payment.processed", {paymentId: '1234', status: 'processed'})