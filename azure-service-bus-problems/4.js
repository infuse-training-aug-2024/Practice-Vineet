// 3. Write a program to receive a message from an Azure Service Bus Queue. Print out the message content and then delete it from the queue.
require("dotenv").config(); 
const { ServiceBusClient } = require("@azure/service-bus");

const connectionString = process.env.CONN_STR;
const queueName = process.env.QUEUE_NAME;

async function main() {  
    const sbClient = new ServiceBusClient(connectionString);
    const receiver = sbClient.createReceiver(queueName, { receiveMode: "peekLock" });

    const messages = await receiver.receiveMessages(1);

    if (messages.length > 0){
        const messageReceived = messages[0];
        console.log(`messageId: ${messageReceived.messageId}`);
        console.log(`correlationId: ${messageReceived.correlationId}`);
        console.log(`body: ${messageReceived.body}`);
        console.log(`deliveryCount: ${messageReceived.deliveryCount}`);

        await receiver.completeMessage(messageReceived);
        console.log("Message processed and removed!")
    }
        
    
    await receiver.close();
    await sbClient.close();

}

main();