#!/usr/bin/node
let row = '';
let column;
let rowString;
const size = parseInt(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (column = 0; column < size; column++) {
    rowString = '';
    for (row = 0; row < size; row++) {
      rowString += 'X';
    }
    console.log(rowString);
  }
}
