#!/usr/bin/node
// Node script that gets the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');
const sourceUrl = process.argv[2];
const storeFile = process.argv[3];

request(sourceUrl, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  fs.writeFile(storeFile, body, 'utf-8', function (err) {
    if (err) {
      console.log(err);
    }
  });
});
