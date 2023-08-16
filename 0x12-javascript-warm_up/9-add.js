#!/usr/bin/node
// A script that prints the addition of 2 integers

const args = process.argv;
const a = args[2];
const b = args[3];
function add (a, b) {
  if (isNaN(a) || isNaN(b)) {
    return (NaN);
  } else {
    return (parseInt(a) + parseInt(b)); // Conversion
  }
}

console.log(add(a, b));
