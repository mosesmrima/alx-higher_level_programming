#!/usr/bin/node

function add (a, b) {
  return console.log(a + b);
}

add(parseInt(process.argv[2], 10), parseInt(process.argv[3], 10));
