const amqp = require("amqplib");

const queue = "task.queue";
const task = {
  message: "Time consuming task",
  sec: 4,
};

async function sendMessage() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  await channel.assertQueue(queue, { durable: true }); // durable: true (Queue Persistance)→ if RabbitMQ restarts, this queue will not be lost.

  channel.sendToQueue(queue, Buffer.from(JSON.stringify(task)), {
    persistent: true,
  }); // persistent: true (Message Persistance) → Messages are written to disk.

  console.log("Sent: ", task);

  setTimeout(() => {
    connection.close();
    process.exit(0);
  }, 500);
}

sendMessage();
