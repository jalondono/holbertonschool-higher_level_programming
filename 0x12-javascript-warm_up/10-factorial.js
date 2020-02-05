#!/usr/bin/node
function factorial (a) {
  if (isNaN(a)) {
    return NaN;
  }
  if (a < 1) {
    return (1);
  }
  return a * (factorial(a - 1));
}
const a = parseInt(process.argv[2]);
let b = 0;
b = factorial(a);
console.log(b);
