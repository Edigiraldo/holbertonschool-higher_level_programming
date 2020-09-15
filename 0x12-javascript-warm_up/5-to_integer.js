#!/usr/bin/node
const arg = process.argv[2];
let message = '';

if (arg === undefined) {
  message = 'Not a number';
} else {
  if (Number.isNaN(parseInt(arg))) {
    message = 'Not a number';
  } else {
    message = 'My number: ' + parseInt(arg);
  }
}
console.log(message);
