#EX1
import numpy as np
from math import *

#EX1
A = np.random.rand(18)
print(A)

#EX2
def relu_numpy(x):
    for i in range(len(x)):
        if(x[i]<0):
            x[i]=0
    return x
print(relu_numpy(np.array([1, -3, 2.5])))

#EX3
def euclidean_norm_numpy(x):
    c=0
    for i in range(len(x)):
        c+=x[i]**2
    c=sqrt(c)
    return c
my_vector = np.array([1,1,1,1])
print(euclidean_norm_numpy(my_vector))

#EX4
def euclidean_norm_2d(X):
    c=0
    for i in range(len(X)):
        for j in range(len(X[i])):
           c+=X[i][j]**2
    c=sqrt(c)
    return c
my_matrix = np.array([[1, -1, 1],
                      [1, 0, 0]])
print(euclidean_norm_2d(my_matrix))


