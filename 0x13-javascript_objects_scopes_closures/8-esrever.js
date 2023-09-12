#!/usr/bin/node

exports.esrever = function (list) {
  const inverse = [];
  for (let i = list.length - 1; i >= 0; i--) {
    inverse.push(list[i]);
  }
  return inverse;
};
