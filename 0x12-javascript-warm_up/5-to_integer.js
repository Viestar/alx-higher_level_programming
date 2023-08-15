#!/usr/bin/node
/*
A script that prints My number: <first argument
converted in integer > if the first argument can be converted to an integers
*/
const args = process.argv;
const number = parseInt(args[2], 10);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${number}`);
}
