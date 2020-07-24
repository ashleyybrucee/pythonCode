'''
CIS 231 Lab 6
Ashley Bruce
08-31-19
'''

import math

def compare (x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    return 0

def hypotenuse (a, b):
    return math.sqrt (a**2 + b**2)

def is_between (x, y, z):
    if x <= y <= z:
        return True
    return False


print (compare (2, 1))
print (compare (1, 2))
print (compare (2, 2))

print (hypotenuse (3, 4))
print (hypotenuse (5, 12))
print (hypotenuse (6, 8))

print (is_between (1, 2, 3))
print (is_between (3, 2, 1))
print (is_between (2, 2, 3))

