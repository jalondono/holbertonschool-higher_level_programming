#!/usr/bin/node
const Request = require('request');
const args = process.argv;
const url = 'http://swapi.co/api/films/' + args[2] + '/';
Request(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    console.log(data.title);
  }
});
