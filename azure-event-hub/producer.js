require('dotenv').config();

const { EventRegistry, QueryArticlesIter } = require("eventregistry");
const { EventHubProducerClient } = require("@azure/event-hubs");

function generate_partitionId() {
    return Math.floor(Math.random() * 2);
}

async function fetchArticlesAboutConcept(flood_number) {
    try {
        const articles = [];
        const er = new EventRegistry({ apiKey: process.env.NEWS_API_KEY });
        const conceptUri1 = await er.getConceptUri("Business");
        
        const q = new QueryArticlesIter(er, { 
            conceptUri: conceptUri1, 
            sortBy: "date",
            dataType: "news",
            maxItems: flood_number,
            lang: "eng",
        });

        
        return new Promise((resolve, reject) => {
            q.execQuery(
                (item) => {
                   
                    articles.push(JSON.stringify(item));
                },
                (error) => {
                    
                    if (error) {
                        reject(new Error(error));
                    } else {
                        
                        resolve(articles);
                    }
                }
            );
        });
    } catch (error) {
        console.error("Error fetching articles:", error);
        return [];
    }
}

async function main() {
    try {
        const article_flood_number = 3;
       
        const articles = await fetchArticlesAboutConcept(article_flood_number);
        
  
        console.log("Fetched Articles:", articles);
        
        
        if (!articles || articles.length === 0) {
            console.error("No articles fetched. Exiting...");
            return;
        }
        
        const producer = new EventHubProducerClient(
            process.env.CONNECTION_STRING, 
            process.env.EVENT_HUB_NAME
        );
        
        const eventDataBatch = await producer.createBatch();
        
        for (let i = 0; i < articles.length; i++) {
            const pid = generate_partitionId();
            const wasAdded = eventDataBatch.tryAdd({ 
                body: articles[i], 
                PartitionKey: pid.toString() 
            });
            
            if (!wasAdded) {
                console.warn("Event batch is full. Sending partial batch...");
                break;
            }
        }
        
        await producer.sendBatch(eventDataBatch);
        await producer.close();
        
        console.log(`A batch of ${articles.length} events have been sent to the event hub`);
    } catch (error) {
        console.error("Error in main function:", error);
    }
}

(async () => {
    try {
        const result = await fetchArticlesAboutConcept(3);
        console.log("Async fetch result:", result);
    } catch (error) {
        console.error("Fetch error:", error);
    }
})();

main();