#!/usr/bin/node

const { argv } = require('node:process');

if (isNaN(argv[2])) {
  console.log('Missing number of occurrences');
} else {
  const repeat = parseInt(argv[2]);

  for (let i = 0; i < repeat; i++) {
    console.log('C is fun');
  }
}
