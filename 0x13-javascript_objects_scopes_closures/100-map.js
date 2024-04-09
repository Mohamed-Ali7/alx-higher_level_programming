#!/usr/bin/node

const list = require('./100-data').list;
let newList = [];

newList = list.map((element, index) => element * index);

console.log(list);
console.log(newList);
