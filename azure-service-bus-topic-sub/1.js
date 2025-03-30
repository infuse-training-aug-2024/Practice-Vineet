require("dotenv").config();
const { delay, ServiceBusClient } = require("@azure/service-bus");
const { appendFile } = require("fs");

const connectionString = process.env.CONN_STR;
const topicName = process.env.TOPIC_NAME;
const subscriptionName = process.env.SUBSCRIPTION_NAME;
const subscriptionName2 = process.env.SUBSCRIPTION_NAME_2;

const single_message = {
    body: "vineet",
    applicationProperties: {
        ["age"]: 20
    }
}


async function send_message_to_topic(){

    const sb_client = new ServiceBusClient(connectionString);
    const sender = sb_client.createSender(topicName);

    try{
        await sender.sendMessages(single_message);
        
        console.log("Message was successfully sent!")
        await sender.close();
    }catch(error){
        console.log("Error while sending message", error);
    }finally{
        await sb_client.close();
    }
}

async function subscriber_consume_1(){
   
    const sb_client = new ServiceBusClient(connectionString);
    const receiver = sb_client.createReceiver(topicName, subscriptionName );
    
    const myMessageHandler = async (messageReceived) => {
        console.log("Tag: s1")
        console.log(`Received message: ${messageReceived.body}`);
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
    await delay(5000);

    await receiver.close();
    await sb_client.close();
}

async function subscriber_consume_2(){
   
    const sb_client = new ServiceBusClient(connectionString);
    const receiver = sb_client.createReceiver(topicName, subscriptionName2);
    
    const myMessageHandler = async (messageReceived) => {
        console.log("Tag: s2")
        console.log(`Received message: ${messageReceived.body}`);
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
    await delay(5000);

    await receiver.close();
    await sb_client.close();
}


function main(){
    send_message_to_topic();
    // subscriber_consume_1();
    // subscriber_consume_2();
}

main();