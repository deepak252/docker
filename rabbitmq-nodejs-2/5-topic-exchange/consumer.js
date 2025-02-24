const amqp = require("amqplib");

const exchange = "logs.topic";
const bindingKey = "logs.*";

const recieveMessage = async () => {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertExchange(exchange, "topic", { durable: false });
  const q = await channel.assertQueue("", { durable: false, exclusive: true });

  await channel.bindQueue(q.queue, exchange, bindingKey);

  channel.consume(
    q.queue,
    (message) => {
      if (message.content) {
        if (message) {
          console.log(
            "Log received: ",
            message.fields.routingKey,
            message.content?.toString()
          );
        }
      }
    },
    { noAck: true }
  );
};

recieveMessage();
