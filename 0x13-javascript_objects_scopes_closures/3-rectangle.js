#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    let j = 0;
    let letter = 'X';
    for (i = 0; i < this.height; i++) {
      letter = '';
      for (j = 0; j < this.width; j++) {
        letter += 'X';
      }
      console.log(letter);
    }
  }
}
module.exports = Rectangle;
