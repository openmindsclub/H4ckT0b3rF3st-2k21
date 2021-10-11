function bubbleSort(array) {
  const length = array.length;
  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      // if number a is greater than number b, swap a with b
      if (array[j] > array[j + 1]) {
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
}

const numbers = prompt("Enter a few numbers separated with a comma.");
if (!numbers || !numbers.includes(",")) {
  alert("Input error. Please make sure to enter numbers and separate each with a comma.");
} else {
  const formattedNumbers = numbers.split(",").map((number) => parseInt(number));
  bubbleSort(formattedNumbers);
  alert(`Sorted list: ${formattedNumbers} `);
}
