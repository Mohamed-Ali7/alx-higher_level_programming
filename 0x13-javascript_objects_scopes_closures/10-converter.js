#!/usr/bin/node

exports.converter = function (base) {
  return function (number) {
    if (base === 16) {
      return toHex(number);
    } else {
      return number;
    }
  };
};

function toHex (number) {
  let temp = number;
  let divider = 1;
  const hexValue = '0123456789abcdef';
  const convertedNum = [];
  let index = 0;

  if (number === 0) {
    return 0;
  }

  while (temp >= 1) {
    temp /= 16;
    if (temp >= 1) {
      divider *= 16;
    }
  }

  while (divider >= 1) {
    index = parseInt((number / divider) % 16);
    convertedNum.push(hexValue[index]);
    divider /= 16;
  }

  return convertedNum.join('');
}
