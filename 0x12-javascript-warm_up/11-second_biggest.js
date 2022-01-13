#!/usr/bin/node

const arr = process.argv.slice(2).map(function (i) {
  return parseInt(i, 10);
}).sort(function (a, b) {
  return a - b;
});

if (arr.length === 0 || arr.length === 1) {
  console.log(0);
} else {
  console.log(arr[arr.length - 2]);
}
