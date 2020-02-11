#!/usr/bin/node
const Request = require('request');
const args = process.argv;
Request(args[2] ,(err, response, body) => {
  if (!err) {
    console.log(`code: ${response.statusCode}`);
  } else {
    console.log(`code: ${err}`);
  }
});
