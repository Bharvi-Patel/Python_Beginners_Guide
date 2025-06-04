# Array - Numpy Arrays:part of the numpy library ,  arrays are designed for high-performance operations on large volumes of data and support multi-dimensional arrays and matrices
# to store multiple items of the same type together.
import numpy as np

arr = np.array([2,5,4,8,6,3,4])
print(arr)
print(arr*2)
# 2-D array
arr1 = np.array([[2,1,4],[3,6,5],[8,7,9]])
print(arr1)
print(arr1/2)
arr2 = np.array([[2,36,52],[0,0,89],[12,36,5]])

a1 = np.zeros((3,3))# Creates an array filles with zeroes
print(a1)
a2 = np.ones((2,3))# Creates an array filled with ones
print(a2)
a3 = np.full((2,2),5)# Creates an array filled with a specific value
print(a3)
a4 = np.eye((4))# Identity matrix
print(a4)
a5 = np.arange(1,10,2)# Creates an array with a range (like range())
print(a5)
a6 = np.linspace(1,10,5)# Creates an array with evenly spaced values
print(a6)
a7 = np.random.rand(3,3)# Generates a random array (uniform distribution)
print(a7)
# a8 = np.random.randint(1,100(3,3))# Generates a random integer array
# print(a8)

# accessing array elements
print(arr[0])

# Shape and reshaping
print(arr1.shape)# Returns the shape (rows, columns) of an array
print(arr1.size)# Returns the total number of elements
print(arr.ndim)# Returns the number of dimensions
print(arr1.reshape(3,3))# Reshapes the array to a different shape
print(arr1.flatten())# Flattens a multi-dimensional array into 1D

# Mathemetical Operations
b1 = np.add(arr1, arr2)# Element-wise addition
print(b1)
b2 = np.subtract(arr1, arr2)# Element-wise subtraction
print(b2)
b3 = np.multiply(arr1, arr2)# Element-wise multiplication
print(b3)
b4 = np.divide(arr1, arr2)# Element-wise division
print(b4)
b5 = np.exp(arr)# Exponential of each element
print(b5)
b6 = np.sqrt(arr)# Square root of each element
print(b6)
b7 = np.log(arr)# Natural logarithm of each element
print(b7)
b8 = np.sin(arr)# Sine of each element
print(b8)

# Statistical Functions
print(np.mean(arr))# Mean (average) of elements
print(np.median(arr))#	Median of elements
print(np.std(arr1))# Standard deviation
print(np.var(arr2))# Variance
print(np.min(arr2))# Minimum value
print(np.max(arr2))# Maximum value
print(np.argmin(arr1))# Index of the minimum value
print(np.argmax(arr))# Index of the maximum value
print(np.sort(arr))# Sorts the array
print(np.split(arr1, 3))# Splits an array into sub-arrays
print(np.concatenate([arr1, arr2]))# Joins arrays along an axis

# using array module
import array as arr
c = arr.array("i",[2,5,25,58,13,0])
print(c)
print(c*2)
k = [12,45,6,9]
print(c.append(96))
print(c.extend(k))# Appends multiple values from an iterable (list, another array, etc.)
print(c.insert(2,21))
print(c.remove(12))
print(c.count(0))# Returns the number of times a value appears in the array
print(c.tolist())# Converts the array to a list      

# slicing
d = arr.array('i', k)
Sliced_array = d[3:8]
print(Sliced_array)

Sliced_array = d[5:]
print(Sliced_array)

Sliced_array = d[:]
print(Sliced_array)

# updating elements
d[2] = 6
print(d)