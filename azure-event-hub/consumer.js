
require('dotenv').config();
const { EventHubConsumerClient, earliestEventPosition } = require("@azure/event-hubs");

async function consumeEventsFromEventHub() {
    try {
        const consumerClient = new EventHubConsumerClient(
            process.env.CONSUMER_GROUP, 
            process.env.CONNECTION_STRING, 
            process.env.EVENT_HUB_NAME
        );

        console.log("Event Hub Consumer Started...");
        const subscription = consumerClient.subscribe({
           
            processEvents: async (events, context) => {
                if (events.length === 0) {
                    console.log("No events received in this batch");
                    return;
                }

                console.log(`Received ${events.length} events`);

                
                events.forEach((event, index) => {
                    try {
                        
                        const eventBody = JSON.parse(event.body);

                        console.log(`Event ${index + 1}:`);
                        console.log('Partition ID:', context.partitionId);
                        console.log('Title:', eventBody.title);
                        console.log('URL:', eventBody.url);
                        console.log('Publication Time:', eventBody.datePublished);

    
                    } catch (parseError) {
                        console.error('Error parsing event:', parseError);
                    }
                });
            },

           
            processError: async (error, context) => {
                console.error(`Error on partition ${context.partitionId}: ${error}`);
            }
        }, {
            
            startPosition: earliestEventPosition
        });

        await new Promise((resolve) => {

            setTimeout(() => {
                subscription.close();
                resolve();
            }, 5 * 60 * 1000); // 5 minutes
        });

        
        await consumerClient.close();
        console.log("Event Hub Consumer Stopped.");

    } catch (error) {
        console.error("Error in Event Hub Consumer:", error);
    }
}

async function consumeFromSpecificPartition() {
    try {
        const consumerClient = new EventHubConsumerClient(
            process.env.CONSUMER_GROUP, 
            process.env.CONNECTION_STRING, 
            process.env.EVENT_HUB_NAME
        );

        
        const partitionIds = await consumerClient.getPartitionIds();
        console.log("Available Partition IDs:", partitionIds);

        
        const specificPartitionConsumer = consumerClient.subscribe(
            partitionIds[0],
            {
                processEvents: async (events) => {
                    events.forEach(event => {
                        console.log('Event on Specific Partition:', 
                            JSON.parse(event.body)
                        );
                    });
                },
                processError: async (error) => {
                    console.error("Partition consumption error:", error);
                }
            },
            earliestEventPosition
        );

        await new Promise(resolve => 
            setTimeout(() => {
                specificPartitionConsumer.close();
                resolve();
            }, 3 * 60 * 1000) // 3 minutes
        );

    } catch (error) {
        console.error("Specific Partition Consumption Error:", error);
    }
}

(async () => {
    try {
        
        await consumeEventsFromEventHub();
    } catch (error) {
        console.error("Consumption Process Error:", error);
    }
})();