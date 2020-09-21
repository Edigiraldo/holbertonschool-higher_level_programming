#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let j = 0; j < this.width; j++) {
      str += 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(str);
    }
  }

  rotate () {
    const aux = this.width;
    this.width = this.height;
    this.height = aux;
  }

  double () {
    this.width = 2 * this.width;
    this.height = 2 * this.height;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let charac = c;
    let str = '';

    if (charac === undefined) {
      charac = 'X';
    }

    for (let j = 0; j < this.width; j++) {
      str += charac;
    }
    for (let i = 0; i < this.height; i++) {
      console.log(str);
    }
  }
}

module.exports = Square;
