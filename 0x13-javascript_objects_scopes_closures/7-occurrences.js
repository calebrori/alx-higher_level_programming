#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOccurences = 0;
  for (let c = 0; c < list.length; c++) {
    if (searchElement === list[c]) {
      nbOccurences++;
    }
  }
  return nbOccurences;
};
