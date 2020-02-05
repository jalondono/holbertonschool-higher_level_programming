#!/usr/bin/node
let i;
exports.addMeMaybe = function (a, b) {
  i = a + 1;
  b(i);
};
