```cpp
#include <vector>
#include <algorithm>

/**
 * @brief Calculates the sequence of reversals needed to sort an array of integers.
 * 
 * This function determines the sequence of reversals required to sort an array of integers
 * in ascending order. It repeatedly finds the index of the smallest element in the unsorted
 * portion of the array and performs two reversals:
 * 1. Reverses the subarray from the beginning to the index of the smallest element.
 * 2. Reverses the subarray from the beginning to the current position of the smallest element.
 *
 * @param arr The input array of integers to be sorted.
 * @return A vector of integers representing the sequence of reversal lengths.
 */
std::vector<int> sort_by_reversals(const std::vector<int>& arr) {
    std::vector<int> reversals;
    std::vector<int> sorted_arr = arr; // Create a copy to avoid modifying the original array
    int n = sorted_arr.size();

    for (int i = 0; i < n - 1; ++i) {
        // Find the index of the minimum element in the remaining unsorted array
        auto min_it = std::min_element(sorted_arr.begin() + i, sorted_arr.end());
        int min_index = std::distance(sorted_arr.begin(), min_it);

        // Perform the reversals only if the minimum element is not already in its correct position
        if (min_index != i) {
            // Reverse the subarray from the beginning to the index of the minimum element
            std::reverse(sorted_arr.begin(), sorted_arr.begin() + min_index + 1);
            reversals.push_back(min_index + 1);

            // Reverse the subarray from the beginning to the current position of the minimum element
            std::reverse(sorted_arr.begin(), sorted_arr.begin() + i + 1);
            reversals.push_back(i + 1);
        }
    }

    return reversals;
}
```

**Unit Tests:**

```cpp
#include "sort_by_reversals.h" // Assuming the function is in a header file "sort_by_reversals.h"
#include <gtest/gtest.h>

TEST(SortByReversalsTest, EmptyArray) {
    std::vector<int> arr = {};
    std::vector<int> expected = {};
    EXPECT_EQ(sort_by_reversals(arr), expected);
}

TEST(SortByReversalsTest, SortedArray) {
    std::vector<int> arr = {1, 2, 3, 4, 5};
    std::vector<int> expected = {};
    EXPECT_EQ(sort_by_reversals(arr), expected);
}

TEST(SortByReversalsTest, ReverseSortedArray) {
    std::vector<int> arr = {5, 4, 3, 2, 1};
    std::vector<int> expected = {5, 4, 3, 2};
    EXPECT_EQ(sort_by_reversals(arr), expected);
}

TEST(SortByReversalsTest, GeneralCase) {
    std::vector<int> arr = {12, 13, 11, 14};
    std::vector<int> expected = {2, 3};
    EXPECT_EQ(sort_by_reversals(arr), expected);
}

TEST(SortByReversalsTest, AnotherGeneralCase) {
    std::vector<int> arr = {4, 2, 5, 1, 3};
    std::vector<int> expected = {2, 4, 3, 5, 2};
    EXPECT_EQ(sort_by_reversals(arr), expected);
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```

**Explanation:**

1. **Function `sort_by_reversals`:**
   - Takes a const reference to the input integer vector `arr`.
   - Creates a copy of the input array `sorted_arr` to avoid modifying the original.
   - Initializes an empty vector `reversals` to store the reversal lengths.
   - Iterates through the array `sorted_arr`, and in each iteration:
     - Finds the index `min_index` of the minimum element in the unsorted portion of the array.
     - If the minimum element is not in its correct position:
       - Reverses the subarray from the beginning to `min_index` and adds `min_index + 1` to `reversals`.
       - Reverses the subarray from the beginning to the current position `i` and adds `i + 1` to `reversals`.
   - Returns the `reversals` vector.

2. **Unit Tests:**
   - The code includes several unit tests using the Google Test framework.
   - Each `TEST` case covers a specific scenario:
     - `EmptyArray`: Tests with an empty input array.
     - `SortedArray`: Tests with an already sorted array.
     - `ReverseSortedArray`: Tests with a reverse sorted array.
     - `GeneralCase`: Tests with the example array provided in the prompt.
     - `AnotherGeneralCase`: Tests with another general unsorted array.
   - `EXPECT_EQ` is used to assert that the output of `sort_by_reversals` matches the `expected` output for each test case.

Remember to include the Google Test library and configure your build system to compile and link the test code.
