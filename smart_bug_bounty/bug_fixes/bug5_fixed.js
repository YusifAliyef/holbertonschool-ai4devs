// Print the numbers 0, 1 and 2, one every 100 milliseconds.
function printNumbers() {
  for (let i = 0; i < 3; i++) {
    setTimeout(function () {
      console.log(i);
    }, i * 100);
  }
}

function main() {
  console.log("Start");
  printNumbers(); // expected output: 0, 1, 2
}

main();
