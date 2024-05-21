#!/usr/bin/node

const exit = require('process').exit;
const argv = require('process').argv;
const request = require('request');

if (argv.length < 3) {
  exit(0);
}

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${argv[2]}/`;

request.get(movieUrl, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const film = JSON.parse(body);

  const characters = film.characters;
  const charactersNames = [];

  for (const characterUrl of characters) {
    charactersNames.push(new Promise((resolve, reject) => {
      request.get(characterUrl, (characterErr, characterRes, characterBody) => {
        if (characterErr) {
          console.log(characterErr);
        }
        const person = JSON.parse(characterBody);
        resolve(person.name);
      });
    }));
  }
  Promise.all(charactersNames).then(names => {
    names.forEach(name => console.log(name));
  });
});
