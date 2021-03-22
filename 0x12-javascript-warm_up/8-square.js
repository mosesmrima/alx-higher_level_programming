#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    let x = '';
    for (let y = 0; y < size; y++) x += 'X';
    console.log(x);
  }
}
