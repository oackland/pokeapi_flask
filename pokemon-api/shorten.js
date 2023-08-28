require('dotenv').config();
const axios = require('axios');
require('dotenv').config();

const longUrl = 'https://example.com'; // Replace with the actual URL

const apiKey = process.env.API_KEY; // Replace with the actual API key

const apiUrl = 'https://api.example-shortener.com/shorten'; // Replace with the actual API endpoint

const headers = {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${apiKey}`
};

axios.post(apiUrl, {url: longUrl}, {headers})
    .then(response => {
        console.log('Shortened URL:', response.data.shortUrl);
    })
    .catch(error => {
        console.error('Failed to shorten URL:', error.message);
        if (error.response) {
            console.error('Response Status:', error.response.status);
            console.error('Response Data:', error.response.data);
        }
    });
