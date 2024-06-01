```cpp
#include <iostream>
#include <vector>

class Matrix {
private:
    int rows;
    int cols;
    std::vector<std::vector<float>> data;

public:
    Matrix(int rows, int cols) : rows(rows), cols(cols), data(rows, std::vector<float>(cols)) {
        std::cout << "Matrix constructor called" << std::endl;
    }

    Matrix(const Matrix& other) : rows(other.rows), cols(other.cols), data(other.data) {
        std::cout << "Matrix copy constructor called" << std::endl;
    }

    Matrix(Matrix&& other) noexcept : rows(other.rows), cols(other.cols), data(std::move(other.data)) {
        other.rows = 0;
        other.cols = 0;
        std::cout << "Matrix move constructor called" << std::endl;
    }

    Matrix& operator=(const Matrix& other) {
        if (this != &other) {
            rows = other.rows;
            cols = other.cols;
            data = other.data;
        }
        std::cout << "Matrix copy assignment operator called" << std::endl;
        return *this;
    }

    Matrix& operator=(Matrix&& other) noexcept {
        if (this != &other) {
            rows = other.rows;
            cols = other.cols;
            data = std::move(other.data);
            other.rows = 0;
            other.cols = 0;
        }
        std::cout << "Matrix move assignment operator called" << std::endl;
        return *this;
    }

    ~Matrix() {
        std::cout << "Matrix destructor called" << std::endl;
    }

    void print() {
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                std::cout << data[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    Matrix mat1(2, 2);
    mat1.print();

    Matrix mat2 = mat1;
    mat2.print();

    Matrix mat3(3, 3);
    mat3 = std::move(mat1);
    mat3.print();

    return 0;
}
```
