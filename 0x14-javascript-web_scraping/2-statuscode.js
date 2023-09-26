#!/usr/bin/node
// Node script that displays the status code of a GET request

const request = require('request');
const sourceUrl = process.argv[2];
request(sourceUrl, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
