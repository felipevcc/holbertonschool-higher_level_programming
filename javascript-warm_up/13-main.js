#!/usr/bin/node
// Call a function that is in another file
const add = require('./13-add').add;
console.log(add(3, 5));
