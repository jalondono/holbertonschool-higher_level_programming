#!/usr/bin/node
let i;
exports.callMeMoby = function (a, b) {
  for (i = 0; i < a; i++) {
    b();
  }
};
