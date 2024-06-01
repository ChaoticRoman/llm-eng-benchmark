Here's a C++ class that stores a two-dimensional float matrix, properly applies the rule of five, takes advantage of move semantics and RVO, and includes debug prints in the special member functions:

```cpp
#include <iostream>
#include <vector>

class Matrix {
private:
    std::vector<std::vector<float>> data;
    int rows;
    int cols;

public:
    // Default constructor
    Matrix() : rows(0), cols(0) {
        std::cout << "Default constructor called" << std::endl;
    }

    // Parameterized constructor
    Matrix(int r, int c) : rows(r), cols(c), data(r, std::vector<float>(c, 0.0f)) {
        std::cout << "Parameterized constructor called" << std::endl;
    }

    // Copy constructor
    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols), data(other.data) {
        std::cout << "Copy constructor called" << std::endl;
    }

    // Move constructor
    Matrix(Matrix&& other) noexcept : rows(other.rows), cols(other.cols), data(std::move(other.data)) {
        std::cout << "Move constructor called" << std::endl;
        other.rows = 0;
        other.cols = 0;
    }

    // Copy assignment operator
    Matrix& operator=(const Matrix& other) {
        std::cout << "Copy assignment operator called" << std::endl;
        if (this != &other) {
            rows = other.rows;
            cols = other.cols;
            data = other.data;
        }
        return *this;
    }

    // Move assignment operator
    Matrix& operator=(Matrix&& other) noexcept {
        std::cout << "Move assignment operator called" << std::endl;
        if (this != &other) {
            rows = other.rows;
            cols = other.cols;
            data = std::move(other.data);
            other.rows = 0;
            other.cols = 0;
        }
        return *this;
    }

    // Destructor
    ~Matrix() {
        std::cout << "Destructor called" << std::endl;
    }

    // Getter for rows
    int getRows() const {
        return rows;
    }

    // Getter for columns
    int getCols() const {
        return cols;
    }

    // Setter for matrix elements
    void setElement(int i, int j, float value) {
        data[i][j] = value;
    }

    // Getter for matrix elements
    float getElement(int i, int j) const {
        return data[i][j];
    }
};

Matrix createMatrix(int rows, int cols) {
    return Matrix(rows, cols);
}

int main() {
    Matrix m1(3, 3);
    m1.setElement(0, 0, 1.0f);
    m1.setElement(1, 1, 2.0f);
    m1.setElement(2, 2, 3.0f);

    Matrix m2 = m1; // Copy constructor
    Matrix m3(std::move(m1)); // Move constructor

    Matrix m4;
    m4 = m2; // Copy assignment operator
    Matrix m5;
    m5 = std::move(m2); // Move assignment operator

    Matrix m6 = createMatrix(4, 4); // RVO

    return 0;
}
```

In this example, the `Matrix` class represents a two-dimensional float matrix. It stores the matrix data using a vector of vectors (`std::vector<std::vector<float>>`). The class implements the rule of five by providing a default constructor, parameterized constructor, copy constructor, move constructor, copy assignment operator, move assignment operator, and destructor.

The class also includes debug print statements in the special member functions to track when they are called.

The `createMatrix` function demonstrates the use of RVO (Return Value Optimization). When returning a `Matrix` object from the function, the compiler can optimize the return by constructing
