#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dict = require('./101-data'); // Update the path accordingly

const initialDict = dict.dict;
const newUserDict = {};

// Create the new dictionary of user ids by occurrence
for (const userId in initialDict) {
  const occurrence = initialDict[userId];
  if (!Object.prototype.hasOwnProperty.call(newUserDict, occurrence)) {
    newUserDict[occurrence] = [];
  }
  newUserDict[occurrence].push(userId);
}

console.log(newUserDict);
