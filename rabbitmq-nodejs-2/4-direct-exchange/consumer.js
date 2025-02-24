const amqp = require("amqplib");

const exchange = "logs.direct";
const bindingKey1 = "logs.info";
const bindingKey2 = "logs.error";
const bindingKey3 = "logs.warning";

const recieveMessage = async () => {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertExchange(exchange, "direct", { durable: false });
  const q = await channel.assertQueue("", { durable: false, exclusive: true });

  // Bind the Queue to Multiple Routing Keys
  // The queue is bound to the exchange multiple times, each with a different routing key.
  // Messages with any of these routing keys will be routed to this queue.
  await channel.bindQueue(q.queue, exchange, bindingKey1);
  await channel.bindQueue(q.queue, exchange, bindingKey2);
  await channel.bindQueue(q.queue, exchange, bindingKey3);

  channel.consume(
    q.queue,
    (message) => {
      if (message) {
        console.log(
          "Log received: ",
          message.fields.routingKey,
          message.content?.toString()
        );
      }
    },
    { noAck: true }
  );
};
recieveMessage();

// const recieveMessage = async () => {
//   const connection = await amqp.connect("amqp://localhost");
//   const channel = await connection.createChannel();

//   await channel.assertExchange(exchange, "direct", { durable: false });
//   await channel.assertQueue(queue, { durable: false, exclusive: true });

//   await channel.bindQueue(queue, exchange, bindingKey);

//   channel.consume(queue, (message) => {
//     if (message) {
//       console.log("Log received: ", message.content?.toString());
//     }
//   }, {noAck: true});
// };

// recieveMessage();
