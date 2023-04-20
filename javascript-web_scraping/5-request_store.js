#!/usr/bin/node
/* Script that gets the contents of a
webpage and stores it in a file */
const URL = process.argv[2];
const file = process.argv[3];
const request = require('request');
const fs = require('fs');

request.get(URL, (error, response, body) => {
  if (!error) {
    fs.writeFile(file, body, error => {
      if (error) console.error(error);
    });
  }
});
