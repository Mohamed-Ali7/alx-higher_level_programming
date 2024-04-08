#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length === 2 || argv.length === 3) {
  console.log(0);
} else {
  let biggest = 0;
  let secondBiggest = 0;

  for (let i = 2; i < argv.length; i++) {
    const cur = parseInt(argv[i]);

    if (cur > biggest) {
      secondBiggest = biggest;
      biggest = cur;
    } else if (cur > secondBiggest) {
      secondBiggest = cur;
    }
  }
  console.log(secondBiggest);
}
