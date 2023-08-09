#!/usr/bin/node
const request = require('request');

function getCharacters(movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const movieData = JSON.parse(body);
        const characters = movieData.characters;
        resolve(characters);
      }
    });
  });
}

async function printCharacterNames(movieId) {
  try {
    const characters = await getCharacters(movieId);
    if (characters.length === 0) {
      console.log('No characters found for the specified movie.');
      return;
    }

    for (const characterUrl of characters) {
      request(characterUrl, (error, response, body) => {
        if (!error && response.statusCode === 200) {
          const characterData = JSON.parse(body);
          const characterName = characterData.name;
          console.log(characterName);
        } else {
          console.log('Error fetching character data from the API');
        }
      });
    }
  } catch (error) {
    console.log('Error fetching data from the API');
  }
}

const args = process.argv.slice(2);
if (args.length !== 1) {
  console.log('Usage: node script.js <movie_id>');
} else {
  const movieId = args[0];
  printCharacterNames(movieId);
}
