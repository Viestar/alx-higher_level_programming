#!/usr/bin/node

// A Rectangle class with a constructor intitialising height and width and creates an empty object incase 0 is passed as a value

module.exports = class Rectangle {
  constructor (w, h) {
    if (w >= 1 && h >= 1) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let index = 0; index < this.height; index++) {
      console.log('X'.repeat(this.width));
    }
  }
};
