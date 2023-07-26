#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const completedTasksByUsers = {};
    body = JSON.parse(body);

    for (let k = 0; k < body.length; ++k) {
      const userId = body[k].userId;
      const completed = body[k].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }

    console.log(completedTasksByUsers);
  }
});
