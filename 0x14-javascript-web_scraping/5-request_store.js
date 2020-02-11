#!/usr/bin/node
const Request = require('request');
const fs = require('fs');
const args = process.argv;
Request (args[2], (err, response, body) => {
  if (!err) {
    fs.writeFileSynk(args[3], body, function(err) {
      if (err) {
        return console.error(err);
      }
    });
  }
});