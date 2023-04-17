#!/usr/bin/node
/* Prints the number of arguments already
printed and the new argument value */
let count = 0;

exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
