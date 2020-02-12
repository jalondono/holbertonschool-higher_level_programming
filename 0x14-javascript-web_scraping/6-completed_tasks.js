#!/usr/bin/node
const Request = require('request');
const args = process.arg;
Request('https://jsonplaceholder.typicode.com/todos', (err, response, body) => {
    data = JSON.parse(body);
    console.log();
})
