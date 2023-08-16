#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

const fs = require('fs');

const sourceFilePath1 = process.argv[2];
const sourceFilePath2 = process.argv[3];
const destinationFilePath = process.argv[4];

const content1 = fs.readFileSync(sourceFilePath1, 'utf8');
const content2 = fs.readFileSync(sourceFilePath2, 'utf8');

const concatenatedContent = content1 + content2;

fs.writeFileSync(destinationFilePath, concatenatedContent, 'utf8');
console.log(concatenatedContent);
