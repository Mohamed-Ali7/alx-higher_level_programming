#!/usr/bin/node

const fs = require('fs');
const exit = require('process').exit;
const argv = require('process').argv;

if (argv.length < 3) {
  exit(0);
}

fs.readFile(argv[2], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
