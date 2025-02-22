const amqp = require("amqplib");

// Email consumer for user
async function recieveUserMail() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  const userQueue = "user_mail_queue";

  await channel.assertQueue(userQueue, { durable: false });

  channel.consume(userQueue, (message) => {
    if (message) {
      console.log('Received message for user', JSON.parse(message.content));
      channel.ack(message); // Acknowledge that message has been received
    }
  });
}
recieveUserMail();
