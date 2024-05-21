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
  const id = '18';
  let count = 0;
  const films = JSON.parse(body).results;

  for (let i = 0; i < films.length; i++) {
    const characters = films[i].characters;

    for (const character of characters) {
      if (character.includes(id)) {
        count++;
      }
    }
  }
  console.log(count);
});
