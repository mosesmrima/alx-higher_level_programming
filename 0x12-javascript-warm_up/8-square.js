#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));
let w;
let h;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (h = 0; h < size; h++) {
    let charS = '';
    for (w = 0; w < size; w++) {
      charS += 'X';
    }
    console.log(charS);
  }
}
