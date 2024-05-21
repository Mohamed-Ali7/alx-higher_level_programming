#!/usr/bin/node

const exit = require('process').exit;
const argv = require('process').argv;
const request = require('request');

if (argv.length < 3) {
  exit(0);
}

request.get(argv[2], (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const usersCompletedTasks = {};

  const tasks = JSON.parse(body);

  for (const task of tasks) {
    if (task.completed) {
      if (task.userId in usersCompletedTasks) {
        usersCompletedTasks[task.userId]++;
      } else {
        usersCompletedTasks[task.userId] = 1;
      }
    }
  }
  console.log(usersCompletedTasks);
});
