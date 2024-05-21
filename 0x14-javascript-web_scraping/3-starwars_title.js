#!/usr/bin/node

const exit = require('process').exit;
const argv = require('process').argv;
const request = require('request');

if (argv.length < 3) {
  exit(0);
}

const url = `https://swapi-api.alx-tools.com/api/films/${argv[2]}`;

request.get(url, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
