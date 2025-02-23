const amqp = require("amqplib");

async function sendMessage() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  setTimeout(() => {
    connection.close();
    process.exit(0);
  }, 500);
}
