#!/usr/bin/node
// Prints x times "C is fun"
const num = parseInt(process.argv[2]);
if (!num) {
  console.log('Missing number of occurrences');
}
for (let i = 0; i < num; i++) {
  console.log('C is fun');
}
