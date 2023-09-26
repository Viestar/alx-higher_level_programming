#!/usr/bin/node
// Node script that reads and prints the content of a file

const fs = require('fs');
const readme_file = process.argv[2];

fs.readFile(readme_file, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
