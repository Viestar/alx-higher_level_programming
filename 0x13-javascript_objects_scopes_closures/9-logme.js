#!/usr/bin/node
// prints the number of arguments.

let items = 0;
exports.logMe = function (item) {
  console.log(items + ': ' + item);
  items++;
};
