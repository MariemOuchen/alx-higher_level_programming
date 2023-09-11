#!/usr/bin/node

const arg1 = process.argv[2];
if (isNaN(arg1)) {
  console.log('Missing size');
} else {
  const side = [];
  for (var i = 0; i < arg1; i++) {
    side[i] = ['X'];

    console.log(side);
}
  for (var i = 0; i < arg1; i++) {
    for (var j = 0; j < arg1; j++) {

      'X';
    }
  }
  console.log(side);

}
