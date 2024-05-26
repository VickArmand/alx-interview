#!/usr/bin/node
/**
 * A script that prints all characters of a Star Wars movie:
 * The first positional argument passed is the Movie ID
 * example: 3 = “Return of the Jedi”
 * Display one character name per line in the same order
 * as the “characters” list in the /films/ endpoint
 * You must use the Star wars API
 * You must use the request module
 */
const req = require('request');
const filmsUrl = 'https://swapi-api.alx-tools.com/api/films/';
req(filmsUrl + process.argv[2], (error, response, body) => {
  if (error) console.log(error);
  else {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});
function printCharacters (characters, index) {
  req(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
