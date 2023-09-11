#!/usr/bin/node

const unSorted = process.argv.slice(2);

if (unSorted[0] === undefined || unSorted.length === 1) {
  console.log(0);
} else {
  const sorted = unSorted.sort((a, b) => a - b);
  console.log(sorted[sorted.length - 2]);
}
