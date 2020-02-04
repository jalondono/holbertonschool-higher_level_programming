#!/usr/bin/node
/**
 * Function to Check if were passed args
 */
const args = process.argv;
if (args.length === 2) {
  console.log('Argument found');
} else if (args.length === 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
