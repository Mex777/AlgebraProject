import time as time
import numpy as numpy


class Matrix:
    __found = {}

    def __init__(self, mat):
        self.mat = numpy.array(mat)
        self.size = len(mat)
        if len(mat) != len(mat[0]):
            raise Exception("The matrix should be square (N x N)")

    # Bubble sorts the lines in the matrix
    # returns the number of swaps that happened in order to know the sign of the determinant
    def num_of_swaps(self, mat):
        sorted_arr = False
        swaps = 0
        while sorted_arr is False:
            sorted_arr = True

            # compares consecutive lines
            # if the next line is lexicographically greater than the current line, it swaps them
            for line in range(0, self.size - 1):
                for col in range(0, self.size):
                    if mat[line][col] < mat[line + 1][col]:
                        sorted_arr = False
                        swaps += 1
                        mat[[line, line + 1]] = mat[[line + 1, line]]
                        break
                    elif mat[line][col] > mat[line + 1][col]:
                        break

        return swaps

    # Computes the determinant of the matrix using the Gauss method
    # factorizes the current line to create a pivot
    # then subtracts the current line from the following ones to create 0s on the current column
    # the determinant is the product of the factors of each line
    def __det_gauss(self):
        mat = self.mat

        # this variable will determine the sign of the determinant
        swaps = self.num_of_swaps(mat)

        # sorts the matrix lines lexicographically decreasing
        sorted_mat = (numpy.flipud(mat[numpy.lexsort(numpy.rot90(mat))])).astype(numpy.float64)

        determinant = 1
        for curr_line in range(0, self.size):
            # we sort the matrix lexicographically if we can't make a pivot on the current line
            if sorted_mat[curr_line][curr_line] == 0:
                swaps += self.num_of_swaps(sorted_mat)
                sorted_mat = numpy.flipud(sorted_mat[numpy.lexsort(numpy.rot90(sorted_mat))])

            factor = sorted_mat[curr_line][curr_line]
            determinant *= factor

            # if the factor was 0 it means that we can't create a pivot
            # therefore the determinant is 0
            if determinant == 0:
                break

            # factorizing the current line
            for j in range(0, self.size):
                sorted_mat[curr_line][j] /= factor

            # subtracting the current line from the following lines
            for next_line in range(curr_line + 1, self.size):
                val_to_subtract = sorted_mat[next_line][curr_line] / sorted_mat[curr_line][curr_line]

                # updating values
                for col in range(0, self.size):
                    sorted_mat[next_line][col] -= sorted_mat[curr_line][col] * val_to_subtract

        if swaps % 2:
            return -determinant
        return determinant

    # Computes the determinant of the matrix using the Laplace method
    # if the matrix is 2x2 we know the answer
    # otherwise we recursively reduce the matrix to a 2x2 using the minors of the current matrix
    def __det_laplace(self, curr_mat):
        # base case
        if curr_mat.shape == (2, 2):
            return curr_mat[0][0] * curr_mat[1][1] - curr_mat[0][1] * curr_mat[1][0]

        # uses memoization to reduce extensive recursive calls
        if str(curr_mat) in self.__found.keys():
            return self.__found[str(curr_mat)]

        curr_det = 0
        for col in range(curr_mat.shape[1]):
            minor_mat = numpy.delete(numpy.delete(curr_mat, 0, 0), col, 1)

            if col % 2 == 0:
                curr_det += curr_mat[0][col] * self.__det_laplace(minor_mat)
            else:
                curr_det -= curr_mat[0][col] * self.__det_laplace(minor_mat)

        self.__found[str(curr_mat)] = curr_det
        return curr_det

    # Measures and returns the time spent computing the determinant using LU factorization
    def get_lu_time(self):
        starting_time = time.time()
        det = numpy.linalg.det(self.mat)
        ending_time = time.time()
        spent_time = round(ending_time - starting_time, 5)

        print(f"Your determinant using LU factorization is {round(det)}. It was found in {spent_time} seconds")
        return spent_time

    # Measures and returns the time spent computing the determinant using Gauss method
    def get_gauss_time(self):
        starting_time = time.time()
        det = self.__det_gauss()
        ending_time = time.time()
        spent_time = round(ending_time - starting_time, 5)

        print(f"Your determinant using Gauss is {round(det)}. It was found in {spent_time} seconds")
        return spent_time

    # Measures and returns the time spent computing the determinant using Laplace method
    def get_laplace_time(self):
        starting_time = time.time()
        det = self.__det_laplace(self.mat)
        ending_time = time.time()
        spent_time = round(ending_time - starting_time, 5)

        print(f"Your determinant using Laplace is {det}. It was found in {spent_time} seconds")
        return spent_time
