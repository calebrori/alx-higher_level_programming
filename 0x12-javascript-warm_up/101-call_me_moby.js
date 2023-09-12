#!/usr/bin/node
exports.callMeMoby = function (d, theFunction) {
  for (let c = 0; c < d; c++) {
    theFunction();
  }
};
