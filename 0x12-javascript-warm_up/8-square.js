#!/usr/bin/node
// a script that prints args times “C is fun”

const args = process.argv[2];
let index = 0;

if (isNaN(args)) {
  console.log('Missing size');
} else {
  for (index; index < args; index++) {
    console.log('X'.repeat(args));
  }
}
