#!/usr/bin/node

const { argv } = require('node:process');
const firstNum = parseInt(argv[2]);
const secondNum = parseInt(argv[3]);

function add (a, b) {
  console.log(a + b);
}

add(firstNum, secondNum);
