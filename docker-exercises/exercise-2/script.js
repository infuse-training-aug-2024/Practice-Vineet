const axios = require('axios');
const moment = require('moment');

const dateInput = process.env.DATE_INPUT || new Date().toISOString();
const formattedDate = moment(dateInput).format('MMMM Do YYYY, h:mm:ss a');

console.log(`Formatted Date: ${formattedDate}`);

const apiUrl = 'https://jsonplaceholder.typicode.com/posts/1';

axios.get(apiUrl)
  .then(response => {
    console.log('API Response:', response.data);
  })
  .catch(error => {
    console.error('Error fetching API:', error);
  });