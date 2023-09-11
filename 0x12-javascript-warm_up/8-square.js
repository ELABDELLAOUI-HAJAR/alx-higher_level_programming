#!/usr/bin/node
const size = Math.floor(Number(process.argv[2]));
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let x = 0; x < size; x++) {
    let line = '';
    for (let y = 0; y < size; y++) {
      line += 'X';
    }
    console.log(line);
  }
}
