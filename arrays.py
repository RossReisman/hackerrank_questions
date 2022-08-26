# First Attempt

import numpy


def arrays(arr):
    arr = numpy.array([input().split()], float)
    return arr[-1:]


arr = input().strip().split(" ")

# Solution

import numpy


def arrays(arr):
    return numpy.array(arr[::-1], float)


arr = input().strip().split(" ")
