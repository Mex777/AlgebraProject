import matplotlib.pyplot as plt

# getting the time data from the file
data_file = open("data.in").readlines()

time_spent_laplace = [float(x) for x in data_file[1].replace("\n", "").split()]
matrix_size_laplace = [int(x) for x in data_file[2].replace("\n", "").split()]

time_spent_gauss = [float(x) for x in data_file[4].replace("\n", "").split()]
matrix_size_gauss = [int(x) for x in data_file[5].replace("\n", "").split()]

time_spent_lu = [float(x) for x in data_file[7].replace("\n", "").split()]
matrix_size_lu = [int(x) for x in data_file[8].replace("\n", "").split()]

# plotting the values using matplotlib
fig, ax = plt.subplots()
ax.plot(matrix_size_gauss, time_spent_gauss, label='Gauss', color="green", linewidth=2)
ax.plot(matrix_size_laplace, time_spent_laplace, label='Laplace', color="blue", linewidth=2)
ax.plot(matrix_size_lu, time_spent_lu, label='LU factorization', color="red", linewidth=2)
ax.set_ylabel("Time in seconds")
ax.set_xlabel("Size of matrix")
plt.legend(prop={'size': 20})
plt.suptitle("Time spent computing the determinant of a matrix", fontsize=30)
plt.show()
