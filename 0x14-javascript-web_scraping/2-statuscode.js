#!/usr/bin/node
// Node script that displays the status code of a GET request

const request = require('request');
const source_url = process.argv[2];
request(source_url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
