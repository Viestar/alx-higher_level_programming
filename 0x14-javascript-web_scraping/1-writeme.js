#!/usr/bin/node
//  Node script that writes a string to a file

const fs = require('fs');
const argv = process.argv;
const write_content = argv[3];
const writeme_file = argv[2];

fs.writeFile(writeme_file, write_content, 'utf-8', function (err) {
  if (err) {
    console.log(err);
  }
});
