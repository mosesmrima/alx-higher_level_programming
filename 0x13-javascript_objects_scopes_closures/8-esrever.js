#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  const newlist = [];
  const len = list.length;
  for (; i < len; i++) {
    newlist[i] = list.pop();
  }
  return newlist;
};
