#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if ((w > 0) && (h > 0)) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      for (let c = 0; c < this.height; c++) {
        let d = '';
        for (let e = 0; e < this.width; e++) {
          d += 'X';
        }
        console.log(s);
      }
    }
  }
  
  module.exports = Rectangle;
  