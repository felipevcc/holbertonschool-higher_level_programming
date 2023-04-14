#!/usr/bin/node
// Prints a msg depending of the argument passed
const num = parseInt(process.argv[2]);
if (num) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
