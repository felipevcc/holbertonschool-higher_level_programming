#!/usr/bin/node
// Searches the secord biggest integer in args
const args = process.argv.slice(2);
if (args.length < 2) {
  console.log(0);
} else {
  let biggest = Number.MIN_SAFE_INTEGER;
  let secBiggest = Number.MIN_SAFE_INTEGER;
  for (let i = 0; i < args.length; i++) {
    const num = parseInt(args[i]);
    if (num > biggest) {
      secBiggest = biggest;
      biggest = num;
    } else if (num > secBiggest) {
      secBiggest = num;
    }
  }
  console.log(secBiggest);
}
