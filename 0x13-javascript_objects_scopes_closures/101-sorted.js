#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new Set(vals)];
const newDict = {};
for (const b in valsUniq) {
  const list = [];
  for (const c in totalist) {
    if (totalist[c][1] === valsUniq[b]) {
      list.unshift(totalist[c][0]);
    }
  }
  newDict[valsUniq[b]] = list;
}
console.log(newDict);
