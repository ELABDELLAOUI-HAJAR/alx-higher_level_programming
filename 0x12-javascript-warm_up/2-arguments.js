#!/usr/bin/node
const process = require('process');
const argLen = process.argv.length - 2;
if (argLen === 0) {
  console.log('No argument');
} else if (argLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
