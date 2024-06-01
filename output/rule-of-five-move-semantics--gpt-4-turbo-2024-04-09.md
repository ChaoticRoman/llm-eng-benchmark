To design a C++ class that manages a two-dimensional float matrix, we'll implement the Rule of Five to properly manage resource allocation and deallocation. This includes a constructor, destructor, copy constructor, copy assignment operator, move constructor, and move assignment operator. We'll also ensure that the class takes advantage of move semantics and Return Value Optimization (RVO) where applicable.

Here's a simple implementation of such a class, named `Matrix`, with debug prints added to each special member function to trace their usage:

```cpp
#include <iostream>
#include <utility> // for std::swap

class Matrix {
private:
    float** data;
    size_t rows, cols;

public:
    // Constructor
    Matrix(size_t r, size_t c) : rows(r), cols(c) {
        data = new float*[rows];
        for (size_t i = 0; i < rows; ++i) {
            data[i] = new float[cols]();
        }
        std::cout << "Constructed Matrix " << this << std::endl;
    }

    // Destructor
    ~Matrix() {
        for (size_t i = 0; i < rows; ++i) {
            delete[] data[i];
        }
        delete[] data;
        std::cout << "Destructed Matrix " << this << std::endl;
    }

    // Copy constructor
    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols) {
        data = new float*[rows];
        for (size_t i = 0; i < rows; ++i) {
            data[i] = new float[cols];
            for (size_t j = 0; j < cols; ++j) {
                data[i][j] = other.data[i][j];
            }
        }
        std::cout << "Copy constructed Matrix " << this << std::endl;
    }

    // Copy assignment operator
    Matrix& operator=(const Matrix& other) {
        if (this != &other) {
            Matrix temp(other);
            std::swap(data, temp.data);
            std::swap(rows, temp.rows);
            std::swap(cols, temp.cols);
        }
        std::cout << "Copy assigned Matrix " << this << std::endl;
        return *this;
    }

    // Move constructor
    Matrix(Matrix&& other) noexcept : data(other.data), rows(other.rows), cols(other.cols) {
        other.data = nullptr;
        other.rows = 0;
        other.cols = 0;
        std::cout << "Move constructed Matrix " << this << std::endl;
    }

    // Move assignment operator
    Matrix& operator=(Matrix&& other) noexcept {
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
        std::cout << "Move assigned Matrix " << this << std::endl;
        return *this;
    }

    // Utility function to print matrix
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
    Matrix mat1(2, 3);
    mat1.print();

    Matrix mat2 = mat1; // Copy constructor
    mat2.print();

    Matrix mat3(3, 2);
    mat3 = mat1; // Copy assignment
    mat3.print();

    Matrix mat4 = std::move(mat1); // Move constructor
    mat4.print();

    Matrix mat5(1, 1);
    mat5 = std::move(mat4); // Move assignment
    mat5.print();

    return 0;
}
```

### Explanation:
1. **Constructor**: Allocates a 2D array of floats.
2. **Destructor**: Deallocates the 2D array.
3. **Copy Constructor**: Performs deep copy.
4. **Copy Assignment Operator**: Uses the copy-and-swap idiom for exception safety.
5. **Move Constructor**: Transfers ownership of resources from the source object, leaving it in a destructible state.
6. **Move Assignment Operator**: Transfers resources and ensures the source object is left in a valid state.

### Debug Prints:
Each special member function prints a message to the console, which helps in tracing the flow of object creation, copying, moving, and destruction.

This implementation ensures efficient management of resources and leverages move semantics to optimize performance, particularly in scenarios involving temporary objects and return values.
