import matrixClass


# Reads a matrix from the user and computes the determinant using Laplace and Gauss methods
def main():
    matrix_size = int(input("Enter the size of the matrix: "))
    matrix = []
    print("Enter the matrix")
    for line in range(matrix_size):
        curr_line = [int(x) for x in input().split()]
        matrix.append(curr_line)

    matrix = matrixClass.Matrix(matrix)
    matrix.get_laplace_time()
    matrix.get_gauss_time()


main()

