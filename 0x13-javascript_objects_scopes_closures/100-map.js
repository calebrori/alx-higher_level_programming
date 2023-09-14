#!/usr/bin/node
const list = require('./100-data.js').list;
console.log(list);
console.log(list.map((module, mark) => module * mark));
