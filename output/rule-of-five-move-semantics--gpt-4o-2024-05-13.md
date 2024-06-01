Certainly! Below is a C++ class that stores a two-dimensional float matrix, properly applies the rule of five, takes full advantage of move semantics, and Return Value Optimization (RVO). Additionally, debug print statements are added to the special member functions to demonstrate their usage.

```cpp
#include <iostream>
#include <vector>
#include <utility>

class FloatMatrix {
public:
    // Default constructor
    FloatMatrix() : rows(0), cols(0), data(nullptr) {
        std::cout << "Default constructor called\n";
    }

    // Parameterized constructor
    FloatMatrix(size_t r, size_t c) : rows(r), cols(c), data(new float[r * c]()) {
        std::cout << "Parameterized constructor called\n";
    }

    // Copy constructor
    FloatMatrix(const FloatMatrix& other) : rows(other.rows), cols(other.cols), data(new float[other.rows * other.cols]) {
        std::cout << "Copy constructor called\n";
        std::copy(other.data, other.data + rows * cols, data);
    }

    // Move constructor
    FloatMatrix(FloatMatrix&& other) noexcept : rows(other.rows), cols(other.cols), data(other.data) {
        std::cout << "Move constructor called\n";
        other.rows = 0;
        other.cols = 0;
        other.data = nullptr;
    }

    // Copy assignment operator
    FloatMatrix& operator=(const FloatMatrix& other) {
        std::cout << "Copy assignment operator called\n";
        if (this == &other) return *this;

        delete[] data;

        rows = other.rows;
        cols = other.cols;
        data = new float[rows * cols];
        std::copy(other.data, other.data + rows * cols, data);

        return *this;
    }

    // Move assignment operator
    FloatMatrix& operator=(FloatMatrix&& other) noexcept {
        std::cout << "Move assignment operator called\n";
        if (this == &other) return *this;

        delete[] data;

        rows = other.rows;
        cols = other.cols;
        data = other.data;

        other.rows = 0;
        other.cols = 0;
        other.data = nullptr;

        return *this;
    }

    // Destructor
    ~FloatMatrix() {
        std::cout << "Destructor called\n";
        delete[] data;
    }

    // Function to set a value in the matrix
    void setValue(size_t r, size_t c, float value) {
        if (r < rows && c < cols) {
            data[r * cols + c] = value;
        }
    }

    // Function to get a value from the matrix
    float getValue(size_t r, size_t c) const {
        if (r < rows && c < cols) {
            return data[r * cols + c];
        }
        return 0.0f;
    }

    // Function to print the matrix
    void print() const {
        for (size_t i = 0; i < rows; ++i) {
            for (size_t j = 0; j < cols; ++j) {
                std::cout << data[i * cols + j] << " ";
            }
            std::cout << "\n";
        }
    }

private:
    size_t rows;
    size_t cols;
    float* data;
};

// Function to create a FloatMatrix and demonstrate RVO
FloatMatrix createMatrix(size_t rows, size_t cols) {
    FloatMatrix matrix(rows, cols);
    for (size_t i = 0; i < rows; ++i) {
        for (size_t j = 0; j < cols; ++j) {
            matrix.setValue(i, j, static_cast<float>(i * cols + j));
        }
    }
    return matrix; // RVO should optimize this
}

int main() {
    std::cout << "Creating matrix A\n";
    FloatMatrix A = createMatrix(3, 3);
    A.print();

    std::cout << "Creating matrix B using copy constructor\n";
    FloatMatrix B = A;
    B.print();

    std::cout << "Creating matrix C using move constructor\n";
    FloatMatrix C = std::move(A);
    C.print();

    std::cout << "Assigning matrix D using copy assignment\n";
    FloatMatrix D;
    D = B;
    D.print();

    std::cout << "Assigning matrix E using move assignment\n";
    FloatMatrix E;
    E = std::move(B);
    E.print();

    return 0;
}
```

### Explanation:
1. **Default Constructor**: Initializes an empty matrix.
2. **Parameterized Constructor**: Initializes a matrix with given dimensions and allocates memory.
3. **Copy Constructor**: Creates a deep copy of another matrix.
4. **Move Constructor**: Transfers ownership of resources from a temporary matrix to a new matrix.
5. **Copy Assignment Operator**: Handles deep copy assignment.
6. **Move Assignment Operator**: Handles move assignment, transferring ownership of resources.
7. **Destructor**: Cleans up allocated memory.

### Demonstration:
- The `main` function demonstrates creating matrices using different constructors and assignment operators.
- The `createMatrix` function demonstrates RVO by returning a `FloatMatrix` object.

This class design ensures efficient resource management and demonstrates the rule of five, move semantics, and RVO in C++.
