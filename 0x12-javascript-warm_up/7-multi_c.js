#!/usr/bin/node
// a script that prints x times “C is fun”

const args = process.argv[2];
let index = 0;

if (isNaN(args)) {
  console.log('Missing number of occurrences');
} else {
  while (index < args) {
    console.log('C is fun');
    index++;
  }
}
