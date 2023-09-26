#!/usr/bin/node
// Node script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const source_url = process.argv[2];
const store_file = process.argv[3];

request(source_url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(store_file, body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
