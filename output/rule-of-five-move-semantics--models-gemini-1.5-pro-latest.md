```cpp
#include <iostream>
#include <vector>
#include <algorithm>

class Matrix {
 public:
  // Default constructor
  Matrix() : rows_(0), cols_(0), data_(nullptr) {
    std::cout << "Default constructor called\n";
  }

  // Parameterized constructor
  Matrix(size_t rows, size_t cols) : rows_(rows), cols_(cols), data_(new float[rows * cols]) {
    std::cout << "Parameterized constructor called\n";
    std::fill_n(data_, rows * cols, 0.0f); // Initialize to zero
  }

  // Copy constructor
  Matrix(const Matrix& other) : rows_(other.rows_), cols_(other.cols_), data_(new float[rows_ * cols_]) {
    std::cout << "Copy constructor called\n";
    std::copy(other.data_, other.data_ + (rows_ * cols_), data_);
  }

  // Move constructor
  Matrix(Matrix&& other) noexcept : rows_(other.rows_), cols_(other.cols_), data_(other.data_) {
    std::cout << "Move constructor called\n";
    other.rows_ = 0;
    other.cols_ = 0;
    other.data_ = nullptr;
  }

  // Destructor
  ~Matrix() {
    std::cout << "Destructor called\n";
    delete[] data_; 
  }

  // Copy assignment operator
  Matrix& operator=(const Matrix& other) {
    std::cout << "Copy assignment operator called\n";
    if (this != &other) { 
      delete[] data_;
      rows_ = other.rows_;
      cols_ = other.cols_;
      data_ = new float[rows_ * cols_];
      std::copy(other.data_, other.data_ + (rows_ * cols_), data_);
    }
    return *this;
  }

  // Move assignment operator
  Matrix& operator=(Matrix&& other) noexcept {
    std::cout << "Move assignment operator called\n";
    if (this != &other) {
      delete[] data_;
      rows_ = other.rows_;
      cols_ = other.cols_;
      data_ = other.data_;

      other.rows_ = 0;
      other.cols_ = 0;
      other.data_ = nullptr;
    }
    return *this;
  }

  // Accessor
  float& operator()(size_t row, size_t col) { 
    return data_[row * cols_ + col]; 
  }

  // Const accessor
  const float& operator()(size_t row, size_t col) const { 
    return data_[row * cols_ + col]; 
  }

  // Matrix addition (example operation, can add more)
  Matrix operator+(const Matrix& other) const {
    if (rows_ != other.rows_ || cols_ != other.cols_) {
      throw std::runtime_error("Matrix dimensions must match for addition.");
    }

    Matrix result(rows_, cols_); // RVO will likely optimize this
    for (size_t i = 0; i < rows_; ++i) {
      for (size_t j = 0; j < cols_; ++j) {
        result(i, j) = (*this)(i, j) + other(i, j);
      }
    }
    return result; 
  }

 private:
  size_t rows_;
  size_t cols_;
  float* data_;
};

int main() {
  // Demonstrate constructors and assignment
  Matrix m1(2, 3); 
  m1(0, 0) = 1;
  m1(1, 2) = 5;

  Matrix m2(m1);  // Copy construction

  Matrix m3;
  m3 = m1;       // Copy assignment

  Matrix m4(std::move(m2)); // Move construction (m2 is now in a valid but unspecified state)
  
  Matrix m5;
  m5 = std::move(m3); // Move assignment (m3 is now in a valid but unspecified state)

  // Demonstrate matrix operations (add more as needed)
  Matrix m6 = m1 + m4;

  return 0;
}
```

**Explanation:**

- **Rule of Five:** The code explicitly implements the destructor, copy constructor, copy assignment operator, move constructor, and move assignment operator.
- **Move Semantics:** Move constructor and move assignment operator efficiently transfer ownership of resources (the `data_` array) without deep copying. They leave the moved-from object in a valid but unspecified state.
- **RVO (Return Value Optimization):** The `operator+` implementation is designed to allow RVO by the compiler. The `result` object is created directly in the function's scope and returned, which often enables the compiler to construct it directly in the caller's memory, eliminating a copy operation.
- **Debug Prints:** Debug messages are included within special member functions to track their invocation during program execution.
- **Error Handling:** Basic error checking is included in `operator+` to ensure matrices have compatible dimensions.

**Output:**

The output will demonstrate the sequence of constructor and assignment operator calls, illustrating the move semantics and potentially showcasing RVO (though compiler optimizations might not always be obvious from the output):

```
Parameterized constructor called
Copy constructor called
Default constructor called
Copy assignment operator called
Move constructor called
Move assignment operator called
Parameterized constructor called // Likely RVO optimized in practice
Destructor called 
Destructor called
... // More destructor calls as objects go out of scope
```

**Key Points:**

- **Resource Management:**  The Rule of Five ensures resources (dynamically allocated memory) are managed correctly, preventing memory leaks.
- **Efficiency:** Move semantics are crucial for performance when working with objects containing dynamically allocated data, as they avoid unnecessary copies.
- **Clarity and Maintainability:**  Explicitly defining the special member functions makes the code more predictable and easier to reason about, particularly when dealing with resource management.
