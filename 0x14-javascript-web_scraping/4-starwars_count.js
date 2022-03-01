#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (!err) {
    const movies = JSON.parse(body).results;
    console.log(movies.reduce((count, movie) => {
      return movie.characters.find((cha) => cha.endsWith('/18/')) ? count + 1 : count;
    }, 0));
  }
});
