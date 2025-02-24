const amqp = require("amqplib");

const exchange = "logs.topic";
const routingKey = "logs.error";
const sendMessage = async () => {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertExchange(exchange, "topic", { durable: false });

  channel.publish(
    exchange,
    routingKey,
    Buffer.from("User created successfully")
  );

  console.log("Log sent");

  setTimeout(() => {
    connection.close();
  });
};

sendMessage();
