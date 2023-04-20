#!/usr/bin/node
/* Script that computes the number
of tasks completed by user id */
const URL = process.argv[2];
const request = require('request');

request(URL, (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const tasksByUser = {}; // Completed tasks
    data.forEach(task => {
      if (task.completed) {
        if (tasksByUser[task.userId]) {
          tasksByUser[task.userId]++;
        } else {
          tasksByUser[task.userId] = 1;
        }
      }
    });
    console.log(tasksByUser);
  }
});
