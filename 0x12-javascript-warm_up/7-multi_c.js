#!/usr/bin/node
let i;
const times = parseInt(process.argv[2]);
const myVar = ['C is fun'];
for (i = 0; i < times; i++) {
  console.log(myVar[0]);
}
