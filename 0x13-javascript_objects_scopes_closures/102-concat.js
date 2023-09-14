#!/usr/bin/node
const files = require('files');

const fArg = files.readFileSync(process.argv[2]).toString();
const sArg = files.readFileSync(process.argv[3]).toString();
files.writeFileSync(process.argv[4], fArg + sArg);
