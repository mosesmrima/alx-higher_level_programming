#!/usr/bin/node

function fac (a) {
  if (isNaN(a)) {
    return 1;
  } else if (a < 0) {
    return -1;
  } else if (a === 0 || a === 1) {
    return 1;
  } else {
    return a * fac(a - 1);
  }
}

const f = fac(parseInt(process.argv[2], 10));
console.log(f);
