#!/usr/bin/node
/**
 * Function to Check if were passed args
 */
const args = process.argv;
const number = parseInt(args[2], 10);
if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
