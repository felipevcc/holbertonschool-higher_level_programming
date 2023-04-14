#!/usr/bin/node
// Prints a square
const size = parseInt(process.argv[2]);
if (!size) {
  console.log('Missing size');
}
for (let i = 0; i < size; i++) {
  for (let j = 0; j < size; j++) {
    process.stdout.write('X');
  }
  console.log('');
}
