#!/usr/bin/node
// Node script that prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const source_url = 'https://swapi-api.hbtn.io/api/films/';
const episode = process.argv[2];

request(source_url + episode, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  console.log(json.title);
});
