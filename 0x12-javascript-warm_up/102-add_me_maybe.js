#!/usr/bin/node
// increments and calls a function.

exports.addMeMaybe = function (num, theFunction) {
  theFunction(num++);
};
