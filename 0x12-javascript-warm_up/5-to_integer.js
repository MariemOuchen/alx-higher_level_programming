#!/usr/bin/node
const stoi = process.argv[2];

if (isNaN(stoi)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(stoi)}`);
}
