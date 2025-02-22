const amqp = require("amqplib");

async function recieveMail() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  const queue = "mail_queue";

  await channel.assertQueue(queue, { durable: false });

  channel.consume(queue, (message) => {
    if (message) {
      console.log(JSON.parse(message.content));
      channel.ack(message); // Acknowledge that message has been received
    }
  });
}
recieveMail();
