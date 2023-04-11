#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const reversedList = [];
  const length = list.length - 1;
  for (let i = length; i >= 0; i--) {
    reversedList.push(list[i]);
  }
  return (reversedList);
};
