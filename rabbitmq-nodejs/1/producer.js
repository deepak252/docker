const amqp = require("amqplib");

async function sendMail() {
  try {
    const connection = await amqp.connect("amqp://localhost");
    const channel = await connection.createChannel();

    const exchange = "mail_exchange";
    const queue = "mail_queue";
    const routingKey = "send_mail";

    const message = {
      to: "user3@gmail.com",
      from: "admin@gmail.com",
      subject: "Hey there",
      body: "Hello",
    };

    await channel.assertExchange(exchange, "direct");
    await channel.assertQueue(queue, { durable: false });
    await channel.bindQueue(queue, exchange, routingKey);
    channel.publish(exchange, routingKey, Buffer.from(JSON.stringify(message)));

    console.log("Mail data sent", message);

    setTimeout(() => {
      connection.close();
    }, 500);
  } catch (e) {
    console.error(e);
  }
}


sendMail()