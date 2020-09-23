#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
const wedge = 'https://swapi-api.hbtn.io/api/people/18/';
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const results = JSON.parse(body).results;
    let counter = 0;
    for (let i = 0; i < results.length; i++) {
      if (results[i].characters.includes(wedge) === true) {
        counter += 1;
      }
    }
    console.log(counter);
  }
});
