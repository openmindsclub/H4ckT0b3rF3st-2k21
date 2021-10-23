// Merge sort is a divide and conquer algorithm.
// It works by breaking down the array into smaller arrays,
// then merging those arrays back together.


function mergeSort(arr) {
    if (arr.length < 2) {
        return arr;
    }

    var middle = Math.floor(arr.length / 2);
    var left = arr.slice(0, middle);
    var right = arr.slice(middle);

    return merge(mergeSort(left), mergeSort(right));
}

function merge(left, right) {
    var result = [];

    while (left.length && right.length) {
        if (left[0] <= right[0]) {
            result.push(left.shift());
        } else {
            result.push(right.shift());
        }
    }

    while (left.length) {
        result.push(left.shift());
    }

    while (right.length) {
        result.push(right.shift());
    }

    return result;
}

console.log(mergeSort([3, 2, 1, 4, 5]));