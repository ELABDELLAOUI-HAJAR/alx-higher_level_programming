#!/usr/bin/node
const argNum = Math.floor(Number(process.argv[2]));
console.log(isNaN(argNum) ? 'Not a number' : `My number: ${argNum}`);
