#!/usr/bin/node
// This script that searches the second biggest integer in the list of arguments.

let maxNumber = 0;
let argsIntArray;
const args = process.argv;
if (args.length >= 2) {
  for (let i = 0; i < args.length; i++) {
    const number = parseInt(args[i]);
    if (isNaN(number)) {
      continue;
    } else {
      argsIntArray[i] = number;
    }
  }
  argsIntArray.sort(); // Sorting and picking second last
  console.log(argsIntArray);
  maxNumber = argsIntArray[argsIntArray.length - 2];
}
console.log(maxNumber);
