#!/usr/bin/node
// Defines a rectangle
class Rectangle {
  constructor (w, h) {
    if (!Number.isInteger(w) || !Number.isInteger(h) || w <= 0 || h <= 0) {
      return {};
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // Prints the rectangle
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
