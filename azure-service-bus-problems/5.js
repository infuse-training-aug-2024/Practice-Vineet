//Write a program to receive a message from an Azure Service Bus Queue using PeekLock mode. After receiving the message, process it and delete it from the queue if processing is successful. If processing fails (e.g., due to a network error), implement retry logic. If the message cannot be processed after a set number of retries (eg. 5), log the failure and move the message to the Dead-letter Queue (DLQ).


/*
Documentation referred:
1) https://learn.microsoft.com/en-us/javascript/api/@azure/service-bus/servicebusreceiver?view=azure-node-latest#@azure-service-bus-servicebusreceiver-deadlettermessage
2) https://learn.microsoft.com/en-us/javascript/api/@azure/service-bus/servicebusreceiver?view=azure-node-latest#@azure-service-bus-servicebusreceiver-receivemessages
*/
require("dotenv").config();
const { ServiceBusClient } = require("@azure/service-bus");


//constants
const connectionString = process.env.CONN_STR;
const queueName = process.env.QUEUE_NAME;
const maxRetries = 5;
const retryDelay = 2000; 

async function main() {
    const sbClient = new ServiceBusClient(connectionString);
    const receiver = sbClient.createReceiver(queueName, { receiveMode: "peekLock" });
  
    try {
      const messages = await receiver.receiveMessages(1, { maxWaitTimeInMs: 5000 });
      
      if (messages.length === 0) {
        console.log("No messages received.");
        await sbClient.close();
        return;
      }
  
      const message = messages[0];
      let retryCount = 0;
      let processed = false;
  
      while (retryCount < maxRetries && !processed) {
        try {
          console.log("Try: ", retryCount);
          console.log("Processing message:", message.body);
  
          // Simulate processing, for example by calling a network API
          await processMessage(message.body);
          
          await receiver.completeMessage(message);
          console.log("Message processed and removed from the queue.");
          processed = true;
  
        } catch (error) {
          retryCount++;
          console.error(`Error processing message (attempt ${retryCount}):`, error.message);
  
          if (retryCount < maxRetries) {
            console.log(`Retrying in ${retryDelay / 1000} seconds...`);
            await delay(retryDelay);
          } else {
            console.log("Max retries reached. Moving message to Dead-letter Queue.");
            await receiver.deadLetterMessage(message);
          }
        }
      }
    } catch (error) {
      console.error("Error receiving messages:", error);
    } finally {
      await sbClient.close();
    }
  }
  
  // Simulated message processing function
  async function processMessage(body) {
    // Simulate a network request failure
    
    if (Math.random() < 0.7) {
      throw new Error("Simulated processing error");
    }
    console.log("Message processed successfully:", body);
  }
  
  function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
  
  main().catch((err) => {
    console.error("Error running main function:", err);
  });