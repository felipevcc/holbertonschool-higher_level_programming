#!/usr/bin/node
// Prints a msg depending of the number of args passed
const args = process.argv;
if (args.length === 3) {
  console.log('Argument found');
} else if (args.length > 3) {
  console.log('Arguments found');
} else {
  console.log('No argument');
}
