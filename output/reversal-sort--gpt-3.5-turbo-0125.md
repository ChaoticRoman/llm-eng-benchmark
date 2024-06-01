```cpp
#include <iostream>
#include <vector>

std::vector<int> reverseSort(std::vector<int> arr) {
    std::vector<int> reversals;
    for (int i = arr.size(); i > 1; i--) {
        int maxIndex = std::distance(arr.begin(), std::max_element(arr.begin(), arr.begin() + i));
        if (maxIndex != i - 1) {
            std::reverse(arr.begin(), arr.begin() + maxIndex + 1);
            reversals.push_back(maxIndex + 1);
            std::reverse(arr.begin(), arr.begin() + i);
            reversals.push_back(i);
        }
    }
    return reversals;
}

void printVector(std::vector<int> vec) {
    for (int i = 0; i < vec.size(); i++) {
        std::cout << vec[i] << " ";
    }
    std::cout << std::endl;
}

int main() {
    std::vector<int> arr = {12, 13, 11, 14};
    std::vector<int> reversals = reverseSort(arr);
    printVector(reversals);

    return 0;
}
```

Documentation:
- `reverseSort` function takes a vector of integers as input and returns a vector of integers representing the reversals needed to sort the array.
- The function iterates through the array and finds the maximum element in the current subarray. If the maximum element is not already at the end of the subarray, it reverses the subarray up to the maximum element and then the entire subarray.
- The function returns a vector of integers representing the indices at which the reversals occurred.

Unit tests:
```cpp
#include "reverseSort.h"
#include <gtest/gtest.h>

TEST(ReverseSortTest, ExampleCase) {
    std::vector<int> arr = {12, 13, 11, 14};
    std::vector<int> expected = {2, 3};
    std::vector<int> result = reverseSort(arr);
    ASSERT_EQ(expected, result);
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
```
