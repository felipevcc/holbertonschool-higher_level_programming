#!/usr/bin/node
/* Converts a number from base 10 to
another base passed as argument */
exports.converter = function (base) {
  return function (number) {
    return number.toString(base);
  };
};
