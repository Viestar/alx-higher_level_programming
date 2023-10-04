#!/usr/bin/node
// Node script that prints all characters of a Star Wars movie

const request = require('request');
const movie = process.argv[2];
const sourceUrl = 'https://swapi-api.hbtn.io/api/people/';

<<<<<<< HEAD
function retrieveCharacters(movie, sourceUrl) {
=======
function retrieve_characters (movie, sourceUrl) {
>>>>>>> 4ed3ec50d46d35cd24b854fda878a9eb55f2eaca
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
      retrieveCharacters(movie, jsonObj.next);
    }
  });
}
retrieveCharacters(movie, sourceUrl);
