#!/usr/bin/node
// Script that display the status code of a GET request
const URL = process.argv[2];
const request = require('request');

request.get(URL, (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
