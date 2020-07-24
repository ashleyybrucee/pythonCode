'''
CIS 231 Lab 7
Ashley Bruce
09-03-19
'''

# Part 1

value = int (input ("Please input a positive integer > "))

sum_of_values = 0
number_of_values_entered = 0
average_value = 0
lowest_number = value
highest_number = value

if (value < 0):
    print ("No valid numbers entered")

else:
    while (value >= 0):
        sum_of_values = sum_of_values + value
        number_of_values_entered += 1
        average_value = round (float (sum_of_values / number_of_values_entered), 2) 
        if lowest_number > value:
            lowest_number = value
        if highest_number < value:
            highest_number = value
    
        value = int (input ("Enter another integer > "))
        
    print ("The sum of all positive values entered is", sum_of_values)
    print ("The number of positive values that were entered is", number_of_values_entered)
    print ("The average of all the positive values entered is", average_value)
    print ("The lowest positive value entered is", lowest_number)
    print ("The highest positive value entered is", highest_number)


# Part 2

import math

def factorial (n):
    if n < 1:
        return 1
    return n * factorial (n-1)

for value in range (5):
    value = int (input ("Please enter a positive integer > "))
    
    while (value < 0):
        value = int (input ("The value entered is negative. Please enter a positive integer > "))
        
    print ("The factorial of the value entered is", factorial (value))

