// 2. Write a program to retrieve messages from an Azure Service Bus Queue. Print out the message details (e.g., message ID, content) without removing the messages from the queue.
require("dotenv").config();
const { delay, ServiceBusClient, ServiceBusMessage } = require("@azure/service-bus");

const connectionString = process.env.CONN_STR;
const queueName = process.env.QUEUE_NAME;

async function main() {
    // create a Service Bus client using the connection string to the Service Bus namespace
    const sbClient = new ServiceBusClient(connectionString);

    // createReceiver() can also be used to create a receiver for a subscription.
    const receiver = sbClient.createReceiver(queueName);

    // function to handle messages
    const myMessageHandler = async (messageReceived) => {
        console.log(`messageId: ${messageReceived.messageId}`);
        console.log(`correlationId: ${messageReceived.correlationId}`);
        console.log(`body: ${messageReceived.body}`);
        console.log(`deliveryCount: ${messageReceived.deliveryCount}`);
    };

    // function to handle any errors
    const myErrorHandler = async (error) => {
        console.log(error);
    };

    // subscribe and specify the message and error handlers
    receiver.subscribe({
        processMessage: myMessageHandler,
        processError: myErrorHandler
    });

    // Waiting long enough before closing the sender to send messages
    await delay(20000);

    await receiver.close();
    await sbClient.close();
}

main()

/*
ref documentation links:
 1) https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-nodejs-how-to-use-queues?tabs=connection-string
 2) https://learn.microsoft.com/en-us/javascript/api/%40azure/service-bus/servicebusmessage?view=azure-node-latest#@azure-service-bus-servicebusmessage-timetolive
 */