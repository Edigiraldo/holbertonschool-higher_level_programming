#!/usr/bin/node
const length = process.argv.length;
let message = '';

if (length === 2) {
  message = 'No argument';
} else if (length === 3) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

console.log(message);
