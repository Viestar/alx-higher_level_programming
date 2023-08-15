#!/usr/bin/node
// imports an array and computes a new array.
const dataModule = require('./100-data'); // Update the path accordingly

const initialList = dataModule.list;
const newList = initialList.map((value, index) => value * index);

console.log('Initial List:', initialList);
console.log('New List:', newList);
