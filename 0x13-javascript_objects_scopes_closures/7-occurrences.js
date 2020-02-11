#!/usr/bin/node
let count = 0;

function countNumber (element, pattern) {
  if (element === pattern) {
    count += 1;
  }
}
exports.nbOccurences = function (list, searchElement) {
  count = 0;
  list.forEach(item => countNumber(item, searchElement));
  return count;
};
