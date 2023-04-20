#!/usr/bin/node
// Script that writes a string to a file
const file = process.argv[2];
const str = process.argv[3];
const fs = require('fs');

fs.writeFile(file, str, err => {
  if (err) {
    console.error(err);
  }
});
