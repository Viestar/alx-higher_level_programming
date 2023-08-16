#!/usr/bin/node
// executes x times a function.
let index = 0;
exports.callMeMoby = function (x, theFunction) {
  while (index < x) {
    theFunction();
    index++;
  }
};
