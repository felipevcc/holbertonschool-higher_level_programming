#!/usr/bin/node
// Prints the first argument passed
const args = process.argv;
if (args[2]) {
  console.log(args[2]);
} else {
  console.log('No argument');
}
