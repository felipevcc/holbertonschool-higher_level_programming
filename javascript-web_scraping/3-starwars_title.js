#!/usr/bin/node
// Script that display the status code of a GET request
const request = require('request');
const movieId = process.argv[2];
const URL = `https://swapi-api.hbtn.io/api/films/${movieId}`;

request.get(URL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
