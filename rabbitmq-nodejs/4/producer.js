const amqp = require("amqplib");

async function sendMessage() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  const exchange = "new_product_launch";

  await channel.assertExchange(exchange, "fanout", { durable: false });

  const message = { message: "New product has been launched" };
  channel.publish(exchange, "", Buffer.from(JSON.stringify(message)), {
    persistent: true,
  });
  console.log("Meage Sent: ", message);

  setTimeout(() => {
    connection.close();
  }, 500);
}

sendMessage();
