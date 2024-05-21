#!/usr/bin/node

const argv = require('process').argv;
const exit = require('process').exit;
const request = require('request');
const fs = require('fs');

if (argv.length < 4) {
  exit(0);
}

const url = argv[2];
const fileName = argv[3];

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
    exit(1);
  }
}
).pipe(fs.createWriteStream(fileName, 'utf-8')
);
