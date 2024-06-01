Below is a C++ function that implements the described sorting algorithm along with a simple test suite using assertions to validate the correctness of the function. The function `sort_by_reversals` sorts an array by repeatedly reversing the order of the first several elements and returns a vector of integers indicating the lengths of the segments reversed at each step.

### C++ Code Implementation

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <cassert>

std::vector<int> sort_by_reversals(std::vector<int>& arr) {
    std::vector<int> steps;
    int n = arr.size();
    
    for (int i = 0; i < n - 1; ++i) {
        // Find the position of the minimum element in the unsorted part
        int min_pos = std::min_element(arr.begin() + i, arr.end()) - arr.begin();
        
        if (min_pos != i) {
            // Reverse the segment from the start to the position of the minimum element
            std::reverse(arr.begin() + i, arr.begin() + min_pos + 1);
            steps.push_back(min_pos - i + 1);
        }
    }
    
    return steps;
}

void test_sort_by_reversals() {
    {
        std::vector<int> test_vec = {12, 13, 11, 14};
        std::vector<int> expected_steps = {2, 3};
        auto steps = sort_by_reversals(test_vec);
        assert(test_vec == std::vector<int>({11, 12, 13, 14}));
        assert(steps == expected_steps);
    }
    
    {
        std::vector<int> test_vec = {4, 3, 2, 1};
        std::vector<int> expected_steps = {4, 3, 2};
        auto steps = sort_by_reversals(test_vec);
        assert(test_vec == std::vector<int>({1, 2, 3, 4}));
        assert(steps == expected_steps);
    }
    
    {
        std::vector<int> test_vec = {1, 2, 3, 4};
        std::vector<int> expected_steps = {};
        auto steps = sort_by_reversals(test_vec);
        assert(test_vec == std::vector<int>({1, 2, 3, 4}));
        assert(steps == expected_steps);
    }
    
    std::cout << "All tests passed!" << std::endl;
}

int main() {
    test_sort_by_reversals();
    return 0;
}
```

### Explanation

1. **Functionality**: The `sort_by_reversals` function sorts the input vector using the specified sorting method. It finds the minimum element in the unsorted part of the array, reverses the segment from the current position to the position of this minimum element, and records the length of the segment reversed.

2. **Testing**: The `test_sort_by_reversals` function contains several test cases to ensure the sorting function works as expected. It checks both the final sorted array and the sequence of reversal steps.

3. **Assertions**: The tests use `assert` to verify that the output from `sort_by_reversals` matches the expected results. If any assertion fails, the program will terminate and indicate the failure.

This implementation and test suite should provide a robust foundation for verifying the correctness of the sorting algorithm described.
