#!/usr/bin/node
// Node script that prints all characters of a Star Wars movie

const request = require('request');
const movie = process.argv[2];
const sourceUrl = 'https://swapi-api.hbtn.io/api/people/';

function retrieve_characters (movie, sourceUrl) {
  request(sourceUrl, function (err, response, body) {
    if (err) {
      console.log(err);
    }
    const jsonObj = JSON.parse(body);
    const characters = jsonObj.results;
    for (const index in characters) {
      for (const index2 in characters[index].films) {
        if (characters[index].films[index2].includes(movie)) {
          console.log(characters[index].name);
        }
      }
    }
    if (jsonObj.next !== null) {
      retrieve_characters(movie, jsonObj.next);
    }
  });
}
retrieve_characters(movie, sourceUrl);
