#!/usr/nin/node
let p = 0;
exports.logMe = function (item) {
  console.log(`${p}: ${item}`);
  p += 1;
};
