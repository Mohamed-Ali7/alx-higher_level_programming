#!/usr/bin/node

const exit = require('process').exit;
const argv = require('process').argv;
const request = require('request');

if (argv.length < 3) {
  exit(0);
}

request.get(argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(`code: ${res.statusCode}`);
});
