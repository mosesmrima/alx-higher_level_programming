#!/usr/bin/node

const num = Math.floor(Number(process.argv[2]));
let i;

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
