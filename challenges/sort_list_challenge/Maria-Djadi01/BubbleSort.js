// Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order.
// The pass through the list is repeated until the list is sorted.
// The algorithm, which is a comparison sort, is named for the way smaller or larger elements "bubble" to the top of the list.
// Bubble sort is a comparison sort, meaning that it can sort items of any type for which a “less-than” relation is defined.
// Bubble sort always takes O(n^2) time.


function bubbleSort(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++) {
            if (array[j] > array[j + 1]) {
                let temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
            }
        }
    }
    return array;
}