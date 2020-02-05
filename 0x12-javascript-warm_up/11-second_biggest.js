#!/usr/bin/node
function convertToNumber (element) {
  numberIntList.push(parseInt(element, 10));
}
let numberStringList = [];
const numberIntList = [];
numberStringList = process.argv.slice(2);
if (numberStringList.length <= 1) {
  console.log(0);
} else {
  numberStringList.forEach(convertToNumber);
  console.log(numberIntList.sort()[numberIntList.length - 2]);
}
