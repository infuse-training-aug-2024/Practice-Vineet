//pls run: docker run -e API_URL='https://jsonplaceholder.typicode.com/posts/1' exercise-2

const axios = require('axios');
const moment = require('moment');
require('dotenv').config();


function getFormattedDate() {
    const dateInput = process.env.DATE_INPUT || new Date().toISOString();
    return moment(dateInput).format('MMMM Do YYYY, h:mm:ss a');
}


function buildApiResponseLog(response) {
    return `API Response: ${JSON.stringify(response.data, null, 2)}`;
}


const apiUrl = process.env.API_URL || 'https://jsonplaceholder.typicode.com/posts/1';


const formattedDate = getFormattedDate();

axios.get(apiUrl)
    .then(response => {
        
        console.log(`Formatted Date: ${formattedDate}\n${buildApiResponseLog(response)}`);
    })
    .catch(error => {
        console.error('Error fetching API:', error);
    });
