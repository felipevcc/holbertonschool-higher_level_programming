#!/usr/bin/node
/* Script that prints the number of movies where the
character "Wedge Antilles" is present (characterID = 18) */
const URL = process.argv[2];
const characterId = 18;
const request = require('request');

request(URL, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body).results;
    const characterMovies = data.filter(movie =>
      movie.characters.some(character =>
        character.endsWith(`/${characterId}/`)
      )
    );
    console.log(characterMovies.length);
  }
});
