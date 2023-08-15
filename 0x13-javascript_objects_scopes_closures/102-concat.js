#!/usr/bin/node
// imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
const dataModule = require('./101-data'); // Update the path accordingly

const initialDict = dataModule.dict;
const newUserDict = {};

// Create the new dictionary of user ids by occurrence
for (const userId in initialDict) {
  const occurrence = initialDict[userId];
  if (!newUserDict.hasOwnProperty(occurrence)) {
    newUserDict[occurrence] = [];
  }
  newUserDict[occurrence].push(userId);
}

console.log(newUserDict);
