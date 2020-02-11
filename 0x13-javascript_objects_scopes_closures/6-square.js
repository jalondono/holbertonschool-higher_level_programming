#!/usr/bin/node
const SquareCons = require('./5-square');

class Square extends SquareCons {
  charPrint (c) {
    let i = 0;
    for (i = 0; i < this.height; i++) {
      if (c != null) {
        console.log(c.repeat(this.width));
      } else {
        console.log('X'.repeat(this.width));
      }
    }
  }
}
module.exports = Square;
