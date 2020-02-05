#!/usr/bin/node
/**
 * foreach loop to print a list
 */
const stringList = ['C is fun', 'Python is cool', 'Javascript is amazing'];
stringList.forEach(function (element, index, array) {
  console.log(element);
});
