#!/usr/bin/node
// Prints the addition of 2 integers
const n1 = parseInt(process.argv[2]);
const n2 = parseInt(process.argv[3]);

function add (a, b) {
  return a + b;
}
const sum = add(n1, n2);
console.log(sum);
