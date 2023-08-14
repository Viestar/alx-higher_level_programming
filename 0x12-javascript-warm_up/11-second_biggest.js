#!/usr/bin/node
// This script that searches the second biggest integer in the list of arguments.

let maxNumber = 0;
const args = process.argv;
if (args.length >= 2) {
    args.sort(); // Sorting and picking second last
    maxNumber = args[args.length - 2];
}
console.log(maxNumber);
