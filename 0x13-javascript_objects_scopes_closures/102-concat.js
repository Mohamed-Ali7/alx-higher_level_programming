#!/usr/bin/node

const fs = require('fs');
const argv = require('process').argv;

const firstFileCont = fs.readFileSync(argv[2], 'utf-8');
const secondFileCont = fs.readFileSync(argv[3], 'utf-8');

fs.writeFileSync(argv[4], `${firstFileCont}${secondFileCont}`);
