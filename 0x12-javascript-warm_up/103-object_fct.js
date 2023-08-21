#!/usr/bin/node
// Added a script that adds a new function that increments the integer value.

const myObject = {
    type: 'object',
    value: 12
};
console.log(myObject);
myObject.incr = function () {
    this.value++;
};
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
