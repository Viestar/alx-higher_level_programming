#!/usr/bin/node
// returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let times = 0;
  for (const indexTwo in list) {
    if (list[indexTwo] === searchElement) {
      times++;
    }
  }
  return times;
};
