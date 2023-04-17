#!/usr/bin/node
// Defines a square and inherits from Rectangle
const ParentSquare = require('./5-square');

class Square extends ParentSquare {
  charPrint (c) {
    // Prints the rectangle using the char "c"
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
