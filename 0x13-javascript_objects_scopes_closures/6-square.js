#!/usr/bin/node

// A class Square that defines a square and inherits from Square of [5-square.js](./5-square.js):
const Squared = require('./5-square');
module.exports = class Square extends Squared {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
  }
};
