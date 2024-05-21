#!/usr/bin/node

const fs = require('fs');
const exit = require('process').exit;
const argv = require('process').argv;

if (argv.length < 4) {
  exit(0);
}

fs.writeFile(argv[2], argv[3], 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
