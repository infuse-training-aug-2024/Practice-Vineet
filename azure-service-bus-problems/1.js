// 1. Write a program to send a message to an Azure Service Bus Queue with a Time-to-Live (TTL) of 2 minutes.
require("dotenv").config();
const { ServiceBusClient } = require("@azure/service-bus");


const connectionString = process.env.CONN_STR;
const queueName = process.env.QUEUE_NAME;

const single_message = {
    body: "vineet",
    timeToLive: 2 * 60 * 1000 
}

async function main() {
    //create a service bus client 
    const sb_client = new ServiceBusClient(connectionString);

    // createSender() can also be used to create a sender for a topic.
    const sender = sb_client.createSender(queueName);

    try {
        await sender.sendMessages(single_message);
        console.log("Message was successfully sent!")
    }catch(error){
        console.log("Error while sending message", error);
    }finally{
        await sender.close();
        await sb_client.close();
    }

}

main();

/*
ref documentation links:
 1) https://learn.microsoft.com/en-us/azure/service-bus-messaging/service-bus-nodejs-how-to-use-queues?tabs=connection-string
 2) https://learn.microsoft.com/en-us/javascript/api/%40azure/service-bus/servicebusmessage?view=azure-node-latest#@azure-service-bus-servicebusmessage-timetolive

*/