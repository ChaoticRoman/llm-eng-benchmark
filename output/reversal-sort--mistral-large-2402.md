Sure, I can help you design a function in C++ that follows this sorting algorithm. The function will return a list of integers corresponding to the required reversals. Here's a simple implementation:

```cpp
#include <vector>
#include <algorithm>
#include <cassert>

std::vector<int> sortByReversals(std::vector<int> arr) {
    std::vector<int> reversals;
    for (int i = 1; i < arr.size(); ++i) {
        if (arr[i] < arr[i - 1]) {
            reversals.push_back(i);
            std::reverse(arr.begin(), arr.begin() + i);
        }
    }
    return reversals;
}
```

This function works by iterating over the array and whenever it finds an element that is less than the previous one, it reverses the order of the first `i` elements and adds `i` to the `reversals` vector.

Here's a simple unit test for this function:

```cpp
void testSortByReversals() {
    std::vector<int> arr = {12, 13, 11, 14};
    std::vector<int> expectedReversals = {2, 3};
    std::vector<int> actualReversals = sortByReversals(arr);
    assert(actualReversals == expectedReversals);
}
```

This test function creates an array `arr` with the values `[12, 13, 11, 14]` and an `expectedReversals` vector with the values `[2, 3]`. It then calls the `sortByReversals` function with `arr` as the argument and stores the result in `actualReversals`. Finally, it asserts that `actualReversals` is equal to `expectedReversals`. If the function is working correctly, this assertion will not cause an error.

Please note that this sorting algorithm is not efficient for large arrays and is mainly used for educational purposes. For practical sorting tasks, it's better to use more efficient algorithms like quicksort, mergesort, or heapsort.

Also, remember to include the necessary headers and use the `assert` macro inside a function to avoid global namespace pollution. The `assert` macro is typically used for debugging and can be disabled in release builds.
