#!/usr/bin/node
// a script that computes and prints a factorial

const number = process.argv[2];
function factorial (number) {
  if (isNaN(number) || number === 1) {
    return (1);
  } else {
    return (number * factorial(number - 1));
  }
}
console.log(factorial(parseInt(number)));
