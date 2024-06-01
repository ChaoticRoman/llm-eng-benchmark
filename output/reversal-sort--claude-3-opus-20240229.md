Here's the implementation of the function in C++ along with documentation and unit tests:

```cpp
#include <vector>
#include <algorithm>

/**
 * Sorts an array of integers by repeatedly reversing the order of the first several elements.
 *
 * @param arr The input array of integers to be sorted.
 * @return A list of integers corresponding to the required reversals.
 */
std::vector<int> sortByReversals(std::vector<int> arr) {
    std::vector<int> reversals;
    int n = arr.size();

    for (int i = 1; i < n; i++) {
        if (arr[i] < arr[i - 1]) {
            int j = i;
            while (j > 0 && arr[j] < arr[j - 1]) {
                j--;
            }
            std::reverse(arr.begin(), arr.begin() + i + 1);
            reversals.push_back(i + 1);
        }
    }

    return reversals;
}
```

Documentation:
The `sortByReversals` function takes an input array of integers `arr` and returns a list of integers corresponding to the required reversals to sort the array.

The function iterates through the array starting from index 1. If the current element is smaller than the previous element, it means the subarray up to the current index needs to be reversed. It finds the correct position `j` where the current element should be inserted by comparing it with the previous elements. Then, it reverses the subarray from the beginning of the array up to index `i + 1` using the `std::reverse` function from the `<algorithm>` library. The size of the reversed subarray `i + 1` is added to the `reversals` list.

The process continues until the entire array is sorted. Finally, the function returns the list of reversals.

Time Complexity: O(n^2), where n is the size of the input array.
Space Complexity: O(n) to store the list of reversals.

Unit Tests:
Here are some unit tests to verify the correctness of the `sortByReversals` function:

```cpp
#include <cassert>
#include <iostream>

void testSortByReversals() {
    // Test case 1
    std::vector<int> arr1 = {12, 13, 11, 14};
    std::vector<int> expected1 = {2, 3};
    std::vector<int> result1 = sortByReversals(arr1);
    assert(result1 == expected1);

    // Test case 2
    std::vector<int> arr2 = {5, 4, 3, 2, 1};
    std::vector<int> expected2 = {2, 3, 4, 5};
    std::vector<int> result2 = sortByReversals(arr2);
    assert(result2 == expected2);

    // Test case 3
    std::vector<int> arr3 = {1, 2, 3, 4, 5};
    std::vector<int> expected3 = {};
    std::vector<int> result3 = sortByReversals(arr3);
    assert(result3 == expected3);

    std::cout << "All test cases passed!" << std::endl;
}

int main() {
    testSortByReversals();
    return 0;
}
```

The unit tests cover different scenarios:
1. Test case 1: An array with a few elements that require reversals.
2. Test case 2: An array in descending order that requires multiple reversals.
3. Test case 3: An array that is already sorted and requires no reversals.

The `assert` statements are used to verify that the
