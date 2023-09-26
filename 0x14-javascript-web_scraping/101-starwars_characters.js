#!/usr/bin/node
// Node script that prints all characters of a Star Wars movie

const request = require('request');
const sourceUrl = 'https://swapi-api.hbtn.io/api/people/';
const movie = process.argv[2];

function retrieve_characters(movie, sourceUrl) {
  request(sourceUrl, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    const obj = JSON.parse(body);
    const characters = obj.results;
    for (const index in characters) {
      for (const index2 in characters[index].films) {
        if (characters[index].films[index2].includes(movie)) {
          console.log(characters[index].name);
        }
      }
    }
    if (obj.next !== null) {
      retrieve_characters(movie, obj.next);
    }
  });
}
retrieve_characters(movie, sourceUrl);
