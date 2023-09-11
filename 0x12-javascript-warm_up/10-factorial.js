#!/usr/bin/node
function factorial (c) {
  if (c < 0) {
    return (-1);
  }
  if (c === 0 || isNaN(c)) {
    return (1);
  }
  return (c * factorial(c - 1));
}

console.log(factorial(Number(process.argv[2])));
