#!/usr/bin/node

if (process.argv[2] === undefined) {
  process.argv[2] = 'undefined';
}

const arg1 = process.argv[2];
const arg2 = process.argv[3];

console.log(arg1.concat(' is ', arg2));
