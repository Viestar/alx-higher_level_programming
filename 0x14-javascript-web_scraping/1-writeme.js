#!/usr/bin/node
//  Node script that writes a string to a file

const fs = require('fs');
const argv = process.argv;
const writeContent = argv[3];
const writemeFile = argv[2];

fs.writeFile(writemeFile, writeContent, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
