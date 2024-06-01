Sure, here's a simple implementation of a 2D matrix class in C++ that follows the rule of five, uses move semantics, and RVO (Return Value Optimization). I've also added some debug prints to special member functions.

```cpp
#include <iostream>
#include <vector>

class Matrix {
public:
    // Constructors
    Matrix() : data_{}, rows_{0}, cols_{0} {
        std::cout << "Default constructor called\n";
    }

    Matrix(size_t rows, size_t cols) : data_(rows * cols, 0.0f), rows_{rows}, cols_{cols} {
        std::cout << "Parameterized constructor called\n";
    }

    // Copy constructor
    Matrix(const Matrix& other) : data_(other.data_), rows_{other.rows_}, cols_{other.cols_} {
        std::cout << "Copy constructor called\n";
    }

    // Move constructor
    Matrix(Matrix&& other) noexcept : data_(std::move(other.data_)), rows_{other.rows_}, cols_{other.cols_} {
        std::cout << "Move constructor called\n";
        other.rows_ = other.cols_ = 0;
    }

    // Destructor
    ~Matrix() {
        std::cout << "Destructor called\n";
    }

    // Copy assignment operator
    Matrix& operator=(const Matrix& other) {
        std::cout << "Copy assignment operator called\n";
        if (this != &other) {
            data_ = other.data_;
            rows_ = other.rows_;
            cols_ = other.cols_;
        }
        return *this;
    }

    // Move assignment operator
    Matrix& operator=(Matrix&& other) noexcept {
        std::cout << "Move assignment operator called\n";
        if (this != &other) {
            data_ = std::move(other.data_);
            rows_ = other.rows_;
            cols_ = other.cols_;
            other.rows_ = other.cols_ = 0;
        }
        return *this;
    }

    // Getters
    size_t rows() const { return rows_; }
    size_t cols() const { return cols_; }

    // Access matrix elements
    float& operator()(size_t row, size_t col) {
        return data_[row * cols_ + col];
    }

    const float& operator()(size_t row, size_t col) const {
        return data_[row * cols_ + col];
    }

private:
    std::vector<float> data_;
    size_t rows_;
    size_t cols_;
};

// Function to demonstrate RVO
Matrix createMatrix(size_t rows, size_t cols) {
    return Matrix(rows, cols);
}

int main() {
    Matrix m1(2, 3);
    m1(0, 0) = 1.0f;
    m1(0, 1) = 2.0f;
    m1(0, 2) = 3.0f;
    m1(1, 0) = 4.0f;
    m1(1, 1) = 5.0f;
    m1(1, 2) = 6.0f;

    Matrix m2 = createMatrix(3, 4);  // RVO

    Matrix m3 = std::move(m1);  // Move assignment

    Matrix m4(m2);  // Copy constructor

    m4 = m3;  // Copy assignment

    return 0;
}
```

This class uses a 1D vector to store the 2D matrix data, which simplifies memory management. The `operator()` function is overloaded to access the matrix elements. The `createMatrix` function demonstrates RVO. The `main` function demonstrates the usage of the class and the different constructors and assignment operators.
