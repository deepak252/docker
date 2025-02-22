const amqp = require("amqplib");

async function sendMail() {
  try {
    const connection = await amqp.connect("amqp://localhost");
    const channel = await connection.createChannel();

    const exchange = "mail_exchange";
    const userQueue = "user_mail_queue";
    const employeeQueue = "employee_mail_queue";
    const userRoutingKey = "send_mail_to_user";
    const employeeRoutingKey = "send_mail_to_employee";

    const isEmployee = false;

    const message = {
      to: "user3@gmail.com",
      from: "admin@gmail.com",
      subject: "Hey there",
      body: "Hello",
    };

    await channel.assertExchange(exchange, "direct");
    await channel.assertQueue(userQueue, { durable: false });
    await channel.assertQueue(employeeQueue, { durable: false });
    await channel.bindQueue(userQueue, exchange, userRoutingKey);
    await channel.bindQueue(employeeQueue, exchange, employeeRoutingKey);

    if(isEmployee){
        channel.publish(exchange, employeeRoutingKey, Buffer.from(JSON.stringify(message)));
    }else{
        channel.publish(exchange, userRoutingKey, Buffer.from(JSON.stringify(message)));
    }

    console.log("Mail data sent", message);

    setTimeout(() => {
      connection.close();
    }, 500);
  } catch (e) {
    console.error(e);
  }
}

sendMail();
