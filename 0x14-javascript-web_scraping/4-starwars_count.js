#!/usr/bin/node
// Node script that prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');
const source_url = process.argv[2];


request(source_url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    for (const index in movies) {
      const characters = movies[index].characters;
      for (const idx in characters) {
        if (characters[idx].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
