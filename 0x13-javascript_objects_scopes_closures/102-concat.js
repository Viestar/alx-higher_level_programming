#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const fs = require('fs');
const path = require('path');

if (process.argv.length !== 5) {
  console.error('Usage: node concatFiles.js <source-file1> <source-file2> <destination-file>');
  process.exit(1);
}

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

try {
  const content1 = fs.readFileSync(sourceFilePath1, 'utf8');
  const content2 = fs.readFileSync(sourceFilePath2, 'utf8');

  const concatenatedContent = content1 + content2;

  fs.writeFileSync(destinationFilePath, concatenatedContent, 'utf8');

  console.log(`Files "${path.basename(sourceFilePath1)}" and "${path.basename(sourceFilePath2)}" concatenated and saved to "${path.basename(destinationFilePath)}".`);
} catch (error) {
  console.error('An error occurred:', error.message);
}
