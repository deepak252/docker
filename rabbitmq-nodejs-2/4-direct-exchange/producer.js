const amqp = require("amqplib");

const exchange = "logs.direct";
// const queue = "logs.queue";
const routingKey = "logs.info";
// const routingKey = "logs.warning";
// const routingKey = "logs.error";

const sendMessage = async () => {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertExchange(exchange, "direct", { durable: false });
  //   await channel.assertQueue(queue, { durable: false });

  channel.publish(
    exchange,
    routingKey,
    Buffer.from("User created successfully")
  );

  setTimeout(() => {
    channel.close();
    process.exit(0);
  }, 500);
};

sendMessage();
