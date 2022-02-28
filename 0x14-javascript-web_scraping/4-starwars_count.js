#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const movies = JSON.parse(body).results;
    let count = 0;
    movies.forEach(movie => {
      movie.characters.forEach(character => {
        if (character.endsWith('/18/')) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
