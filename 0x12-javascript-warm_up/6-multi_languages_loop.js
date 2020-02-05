#!/usr/bin/node
/**
 * foreach loop to print a list
 */
const Stringlist = ['C is fun', 'Python is cool', 'Javascript is amazing'];
Stringlist.forEach(function (element, index, array) {
  console.log(element);
});
