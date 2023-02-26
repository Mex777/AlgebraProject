import matrixClass
import numpy

matrix_size = []
time_spent_gauss = []
time_spent_lu = []
time_spent_laplace = []

# creating some random i x i matrices to measure the time spent computing the determinant using Laplace method
for i in range(2, 13):
    matrix = matrixClass.Matrix(numpy.random.randint(5, size=(i, i)))
    time_spent_laplace.append(matrix.get_laplace_time())

# creating some random i x i matrices to measure the time spent computing the determinant using Gauss method and LU factorization
for i in range(2, 100):
    matrix = matrixClass.Matrix(numpy.random.randint(2, size=(i, i)))
    time_spent_lu.append(matrix.get_lu_time())
    time_spent_gauss.append(matrix.get_gauss_time())
    matrix_size.append(i)

file = open("data.in", "w")

# writing the data for Laplace
file.write("Laplace:\n")
for curr_time in time_spent_laplace:
    file.write(f"{curr_time} ")
file.write("\n")
for size in range(len(time_spent_laplace)):
    file.write(f"{size + 2} ")
file.write('\n')

# writing the data for Gauss
file.write("Gauss:\n")
for curr_time in time_spent_gauss:
    file.write(f"{curr_time} ")
file.write("\n")
for size in range(len(time_spent_gauss)):
    file.write(f"{size + 2} ")
file.write('\n')

# writing the data for Gauss
file.write("LU factorization:\n")
for curr_time in time_spent_lu:
    file.write(f"{curr_time} ")
file.write("\n")
for size in range(len(time_spent_lu)):
    file.write(f"{size + 2} ")

file.close()
