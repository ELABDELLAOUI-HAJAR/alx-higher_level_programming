#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbIccur = 0;
  for (const elmt in list) {
    if (list[elmt] === searchElement) nbIccur++;
  }
  return nbIccur;
};
