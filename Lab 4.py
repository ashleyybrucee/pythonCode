## Ashley Bruce
## Lab 4
## CIS 231
## 8/24/19

import math


## Functions

def name_five_times (name):
    for i in range (5):
        print (name)
     
def name_choose_times (name, number):
    for i in range (number):
        print (name)
        
def hypotenuse_of_triangle (a, b):
    c = math.sqrt (a**2 + b**2)
    print ("The hypotenuse of a right triangle with sides", a, "and", b, "is", c)

def quadratic_equation_solutions (a, b, c):
    plus_squareroot = (-b + math.sqrt (b**2 - 4*a*c) ) / (2*a)
    minus_squareroot = (-b - math.sqrt (b**2 - 4*a*c) ) / (2*a)
    print ("If a is", a, ", b is", b, ", and c is", c)
    print ("    the answers to the quadratic formula are", plus_squareroot, "and", minus_squareroot)


## Function Test Cases

name_five_times ('Ashley')
name_five_times ('Kim')
name_five_times ('Ryan')

name_choose_times ('Bob', 2)
name_choose_times ('Hailey', 4)
name_choose_times ('Caitlin', 6)

hypotenuse_of_triangle (3, 4)
hypotenuse_of_triangle (5, 12)
hypotenuse_of_triangle (6, 8)

quadratic_equation_solutions (1, 3, -4)
quadratic_equation_solutions (2, -8, -24)
quadratic_equation_solutions (1, 8, 15)
