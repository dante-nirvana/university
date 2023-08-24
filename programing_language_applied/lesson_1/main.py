# Libraries and Versioning

# Installing and using numpy:

# 1 - Download and install dependencies using package installer for python (pip)
# this module will be using NUMPY and PLOTLY.

# Then import the library with the command import numpy as np

# Remember to uncomment import command for each part if necessary

# import numpy as np
# import time as t
# import plotly.express

# Now some examples on how to use numpy and it's features

# Note: numpy arrays works with statically typed variables to create arrays, wich means
# that all of it's indexes are from same type

# ndarray1 = np.zeros(100000) # creates an array with 100 thousand indexes filled with 0
# print(f"Content of the array: {ndarray1}, it's size: {len(ndarray1)}")

# ndarray1 = np.ones(100000) # same thing, but with ones instead of zeros
# print(f"Content of the array: {ndarray1}, it's size: {len(ndarray1)}")

# ndarray1 = np.linspace(10, 1000, 1000)
# # line above generates numbers from 10 to 1000 with 1000 elements

# print(f"Content of the array:\n{ndarray1},\n it's size: {len(ndarray1)}")

# 2 - Some performance comparison

# # Numpy...
# start_time1 = t.time()
# ndarray = np.zeros(100000000)
# end_time1 = t.time()
# elapsed_time1 = end_time1 - start_time1
# print(f"\nNumpy creates an array with 1 billion elements \
# (filled with zeros) in: {elapsed_time1}")

# # Python regular libs
# start_time = t.time()
# regular_list = [0] * 100000000
# end_time = t.time()
# elapsed_time = end_time - start_time
# print(f"\nRegular Python list structure creates an array with 1 billion elements \
# (filled with zeros) in: {elapsed_time}")

# 3 - Stating a type and size for data will increase performance even further...

# start_time = t.time()
# ndarray = np.zeros(1000000000, dtype='uint8')
# end_time = t.time()
# elapsed_time = end_time - start_time
# print(f"Numpy creates an array with 1 billion elements \
# (filled with zeros) in: {elapsed_time}\n")

# 4 - Creating multidimessional arrays

# rng = np.random.default_rng() # numpy has its own random methods
# array_1d = rng.random(4)
# array_2d = rng.random([4, 4])
# array_3d = rng.random([4, 4, 4])
# print(f' 1 dimenssion with random values:\n\n{array_1d}\n')
# print(f' 2 dimenssion with random values:\n\n{array_2d}\n')
# print(f' 3 dimenssion with random values:\n\n{array_3d}\n')

# 5 - Sorting with numpy

# rng = np.random.default_rng()
# array_2d = rng.random([4, 4])
# array_column = np.sort(array_2d, axis=0)
# array_line = np.sort(array_2d, axis=1)
# array_column_and_line = np.sort(array_line, axis=0)
# print(f'Sorting by columns:\n{array_column}')
# print(f'Sorting by lines:\n{array_line}')
# print(f'Sorting by columns and lines:\n{array_column_and_line}')

# 6 - Ploting ndarrays with plotly library

# array_a = np.linspace(10, 1000, 100)
# array_b = np.linspace(10, 3000, 100)
# array_c = np.linspace(10, 8000, 100)

# # print(array_a)
# # print(array_b)
# # print(array_c)

# # using numpy to save files .txt
# np.savetxt('array_a.txt', array_a, fmt='%f', delimiter=';')
# np.savetxt('array_b.txt', array_b, fmt='%f', delimiter=';') 
# np.savetxt('array_c.txt', array_c, fmt='%f', delimiter=';')

# array_a = np.loadtxt('array_a.txt', dtype=np.float64, delimiter=';')
# array_b = np.loadtxt('array_b.txt', dtype=np.float64, delimiter=';')
# array_c = np.loadtxt('array_c.txt', dtype=np.float64, delimiter=';')

# # print(array_a)

# array_abc = np.vstack([array_a, array_b, array_c])
# # print(array_abc)
# array_abc = array_abc.transpose()
# # print(array_abc)
# fig = plotly.express.line(array_abc)
# fig.show()
