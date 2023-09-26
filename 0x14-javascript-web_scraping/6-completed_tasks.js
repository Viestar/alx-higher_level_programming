#!/usr/bin/node
// Node script that computes the number of tasks completed_tasks by user id

const request = require('request');
const url = process.argv[2];
const completed_tasks = {};

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    for (const index in tasks) {
      const task = tasks[index];
      if (task.completed_tasks === true) {
        if (completed_tasks[task.userId] === undefined) {
          completed_tasks[task.userId] = 1;
        } else {
          completed_tasks[task.userId]++;
        }
      }
    }
    console.log(completed_tasks);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
