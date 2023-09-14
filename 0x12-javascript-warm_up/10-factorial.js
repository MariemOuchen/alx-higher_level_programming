#!/usr/bin/node

const a = parseInt(process.argv[2]);

function fact (a) {
  if (a < 0) {
    return -1;
  } else if (a === 0 || isNaN(a)) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}

console.log(fact(a));
