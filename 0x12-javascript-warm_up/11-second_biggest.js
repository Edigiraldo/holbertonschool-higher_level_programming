#!/usr/bin/node
const args = process.argv;
const length = args.length;

if (length === 2 || length === 3) {
  console.log(0);
} else {
  console.log(parseInt(args[3]));
}
