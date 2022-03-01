#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}/`;

request(url, (err, res, body) => {
  if (!err) {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      request(characters[i], (err1, res1, body1) => {
        if (!err1) {
          console.log(JSON.parse(body1).name);
        }
      });
    }
  }
});
