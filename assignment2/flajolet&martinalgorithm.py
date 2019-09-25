# -*- coding: utf-8 -*-
"""Flajolet&MartinAlgorithm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Rv7zD_1vi4xDSZcwH2tzw-RzM-D7FIkp

# Assignment 2
## Create a Flajolet and Martin Algorithm implementation

The objective of this assignment is to create an implementation for a Flajolet and Martin Algorithm for a variable data stream. For this purpose, the first step is to install and import the needed libraries: numpy, random, math and bitarray.
"""

!pip install bitarray

import numpy as np
import random
import math
from bitarray import bitarray

"""Once this part is done, the next step is to ask the user to enter a number for the size of the bitmap (array of bits). Then, another number for the amount of samples generated. Finally, a third number for the highest value supported in the data stream that it is going to be created randomly."""

n = int(input("Enter a number for the size of the bitmap, in bits: "))
m = int(input("Enter a number for the amount of samples generated: "))
l = int(input("Enter a number for the highest value supported in the generated data stream: "))

"""Now, we set a constant value phi equal to 0.77351, and we initialize the bitmap to zero in every position."""

phi = 0.77351

bitmap = n * bitarray('0')
print(bitmap)

"""After the bitmap is initialized to zero, it is possible to create the random data stream within a list and then print it."""

stream = []

for i in range(0,m):
    x = random.randint(1,l)
    stream.append(x)

print(stream)

"""It is also required to define a way to compute the least significant one for a binary representation, so it is created a function called least_significant_one, which returns the position of the array in which the least significant one is."""

def least_significant_one(x):
  for i in range(len(x)-1,-1,-1):
    if x[i] == 1:
      return i
  return len(x)-1

"""Finally, it is time to run a for loop that firstly computes a hash function randomly defined. Afterwards, computes the binary representation of such result. Once it is obtained such binary representation, it is used the previously defined function least_significant_one to get the position that fulfills this requirement. The last step is to set the bitmap's bit which corresponds to that position. Then, the loop is closed and the bitmap is printed after the whole process."""

for i in stream:
  h = (7*i+83) % 74
  b = format(h, "b")
  index = least_significant_one(b)
  if bitmap[len(bitmap)-index-1] == 0:
    bitmap[len(bitmap)-index-1] = 1

print(bitmap)

"""The final step before calculating the results is to define R, which is the highest index in which the bitmap index is 1. It is created a loop that calculates this number and then it is printed out."""

r = 0

for i in range(len(bitmap)):
  if bitmap[i] == 1:
    r = len(bitmap)-1-i
    break

print(r)

"""The results achieved for this trial of the Flajolet and Martin Algorithm are the following ones:"""

cardinality = (2**r)/phi
print("The cardinality of M, output of the algorithm, is: {0}".format(cardinality))
print("The actual number of different values in the data stream M is: {0}".format(len(np.unique(stream))))

"""In my opinion, it is not easy to produce efficient results trying this algorithm, unless the hash function fits perfectly with the solution. There is always a considerable difference between the cardinality computed with the algorithm, and the one expressed by the length of the numpy function unique."""