To design a C++ class that meets your requirements, we'll create a class named `Matrix` that encapsulates a two-dimensional float matrix. This class will properly implement the Rule of Five, which includes a destructor, copy constructor, copy assignment operator, move constructor, and move assignment operator. We'll ensure it takes full advantage of move semantics and Return Value Optimization (RVO) to optimize performance. Additionally, we'll add debug prints to special member functions to demonstrate their usage.

Here's an example implementation:

```cpp
#include <iostream>
#include <utility> // For std::swap

class Matrix {
private:
    float** data;
    size_t rows, cols;

public:
    // Constructor
    Matrix(size_t rows, size_t cols) : rows(rows), cols(cols), data(new float*[rows]) {
        std::cout << "Constructor called\n";
        for (size_t i = 0; i < rows; ++i) {
            data[i] = new float[cols]{};
        }
    }

    // Destructor
    ~Matrix() {
        std::cout << "Destructor called\n";
        for (size_t i = 0; i < rows; ++i) {
            delete[] data[i];
        }
        delete[] data;
    }

    // Copy constructor
    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols), data(new float*[other.rows]) {
        std::cout << "Copy constructor called\n";
        for (size_t i = 0; i < rows; ++i) {
            data[i] = new float[cols];
            for (size_t j = 0; j < cols; ++j) {
                data[i][j] = other.data[i][j];
            }
        }
    }

    // Copy assignment operator
    Matrix& operator=(const Matrix& other) {
        std::cout << "Copy assignment operator called\n";
        if (this != &other) {
            Matrix temp(other);
            std::swap(rows, temp.rows);
            std::swap(cols, temp.cols);
            std::swap(data, temp.data);
        }
        return *this;
    }

    // Move constructor
    Matrix(Matrix&& other) noexcept : data(nullptr), rows(0), cols(0) {
        std::cout << "Move constructor called\n";
        *this = std::move(other);
    }

    // Move assignment operator
    Matrix& operator=(Matrix&& other) noexcept {
        std::cout << "Move assignment operator called\n";
        if (this != &other) {
            for (size_t i = 0; i < rows; ++i) {
                delete[] data[i];
            }
            delete[] data;

            data = other.data;
            rows = other.rows;
            cols = other.cols;

            other.data = nullptr;
            other.rows = 0;
            other.cols = 0;
        }
        return *this;
    }

    // Example usage of the class
    void print() const {
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                std::cout << data[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    Matrix m1(3, 3); // Constructor
    Matrix m2 = m1; // Copy constructor
    Matrix m3(2, 2); // Constructor
    m3 = m1; // Copy assignment operator
    Matrix m4 = std::move(m1); // Move constructor
    m3 = std::move(m4); // Move assignment operator

    // m1 is in a moved-from state, so we don't use it here
    m2.print();
    m3.print();
    // Destructor called for m2, m3, m1 (in moved-from state), and m4 (in moved-from state)
    return 0;
}
```

This example demonstrates a class that manages a 2D float matrix with proper resource management, adhering to the Rule of Five. It includes debug print statements in each special member function to track their calls. The `main` function illustrates various uses of the class, including copy and move operations. Note that after a move operation, the moved-from object is in a valid but unspecified state, so it's not used further except for destruction.
