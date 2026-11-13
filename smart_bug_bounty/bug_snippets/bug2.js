// Calculate the average of an array of numbers.
function average(numbers) {
  if (numbers.length === 0) {
    return 0;
  }
  let sum = 0;
  for (let i = 0; i <= numbers.length; i++) {
    sum += numbers[i];
  }
  return sum / numbers.length;
}

function main() {
  console.log(average([2, 4, 6])); // expected 4
  console.log(average([10]));      // expected 10
  console.log(average([]));        // expected 0
}

main();
