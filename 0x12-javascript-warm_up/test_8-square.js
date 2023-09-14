#!/usr/bin/node

const arg1 = process.argv[2];
if (isNaN(arg1)) {
  console.log('Missing size');
} else {
  parseInt(arg1);
  const side = new Array(arg1);

  for (var i = 0; i < arg1; i++) {
    side[i] = new Array(arg1);

    for (var j = 0; j < arg1; j++) {
      side[i][j] = 'X';
    }
  }
  console.log(side);
}
