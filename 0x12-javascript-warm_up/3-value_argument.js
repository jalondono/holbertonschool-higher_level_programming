#!/usr/bin/node
/**
 * Function to Check if were passed args
 */
const args = process.argv;
if (args[2] === undefined) {
  console.log('Argument found');
} else {
  console.log(args[2]);
}
