#!/usr/bin/node
const Request = require('request');
const args = process.argv;
const url = args[2];
let number = 0;
Request(url, (err, response, body) => {
  if (!err) {
    const data = JSON.parse(body);
    let actor = [];
    data.results.forEach(item => {
      for (actor of item.characters) {
        if (actor.match('/18/')) {
          number++;
        }
      }
    });
    console.log(number);
  }
});
