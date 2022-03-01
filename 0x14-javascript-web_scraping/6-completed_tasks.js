#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (!err) {
    const myObj = {};
    const tasks = JSON.parse(body);
    for (const task of tasks) {
      if (task.completed) {
        myObj[task.userId] = myObj[task.userId] ? myObj[task.userId] + 1 : 1;
      }
    }
    console.log(myObj);
  }
});
