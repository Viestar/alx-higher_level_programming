#!/usr/bin/node
// A script that prints the first argument passed.
const args = process.argv[2]
if (args === undefined) {
    console.log("No argument")
} else {
    console.log(args);
}


