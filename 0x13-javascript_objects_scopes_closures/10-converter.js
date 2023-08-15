#!/usr/bin/node
// Converts a number to any given base
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
