#!/usr/bin/node
// a script that prints x times “C is fun”

const args = process.argv[2];
let index = 0;
while (index < args) {
    console.log("C is fun");
    index++;
}
