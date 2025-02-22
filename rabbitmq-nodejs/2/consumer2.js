const amqp = require("amqplib");

// Email consumer for employee
async function recieveMail() {
  const connection = await amqp.connect("amqp://localhost");
  const channel = await connection.createChannel();

  const employeeQueue = "employee_mail_queue";

  await channel.assertQueue(employeeQueue, { durable: false });

  channel.consume(employeeQueue, (message) => {
    if (message) {
      console.log("Received message for employee", JSON.parse(message.content));
      channel.ack(message); // Acknowledge that message has been received
    }
  });
}
recieveMail();
