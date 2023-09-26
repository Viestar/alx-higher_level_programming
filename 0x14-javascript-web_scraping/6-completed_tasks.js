#!/usr/bin/node
// Node script that computes the number of tasks completedTasks by user id

const request = require('request');
const url = process.argv[2];
const completedTasks = {};

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    for (const index in tasks) {
      const task = tasks[index];
      if (task.completedTasks === true) {
        if (completedTasks[task.userId] === undefined) {
          completedTasks[task.userId] = 1;
        } else {
          completedTasks[task.userId]++;
        }
      }
    }
    console.log(completedTasks);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});
