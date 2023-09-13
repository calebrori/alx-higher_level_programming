#!/usr/bin/node
exports.esrever = function (list) {
  let len = list.length - 1;
  let c = 0;
  while ((len - c) > 0) {
    const aux = list[len];
    list[len] = list[i];
    list[i] = aux;
    c++;
    len--;
  }
  return list;
};
