
var path = require("path");

var Hello = "hello from node JS"
console.log(`printing variable hello: ${Hello}`);

console.log("directory name: " + __dirname);
console.log("directory and file name: " + __filename)

console.log("using PATH module");
console.log(`hello from file ${path.basename(__filename)}`);

console.log(`process arge: ${process.argv}`);