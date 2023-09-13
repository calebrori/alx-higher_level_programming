#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let f = 0; f < this.height; f++) {
      let d = '';
      for (let e = 0; e < this.width; e++) {
        d += c;
      }
      console.log(d);
    }
  }
}

module.exports = Square;
