#!/usr/bin/node
function factorial (a) {
  if (!a || isNaN(a)) {
    return (1);
  }
  if (a === 1) {
    return (1);
  }
  return a * (factorial(a - 1));
}
console.log(factorial(parseInt(process.argv[2])));
