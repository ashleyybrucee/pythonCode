'''
CIS 231 Lab 10
Ashley Bruce
09-18-19
'''

import math


#functions

def is_int_valid (number):
    try:
        value = int (number)
    except ValueError:
        return False
    else:
        return True


def is_int_in_range (number):
    number = float (number)
    if (number < 1 or number > 15):
        return False
    else:
        return True


def input_nums (numValues):
    print ("\nPlease enter", numValues, "values, one at a time, as you are prompted to.")
    print ("Values do not have to be integers and can be positive or negative.")
    number_list = []
    for number in range (numValues):
        value = float (input ("Please enter a value > "))
        number_list.append (value)
    return number_list


def in_order (a_list):
    print ("\nHere all the values you input in order:")
    for number in a_list:
        print ("%.1f" % (number))


def rev_order (a_list):
    print ("\nHere are the values you input in reverse order:")
    for number in a_list [::-1]:
        print ("%.1f" % (number))


def abo_bel_equ (a_list, number_values):
    sum_num = 0
    below_average = 0
    above_average = 0
    on_average = 0
    
    for number in a_list:
        sum_num = sum_num + number

    numbers_average = sum_num / number_values

    for number in a_list:
        if number > numbers_average:
            above_average = above_average + 1
        if number < numbers_average:
            below_average = below_average + 1
        if number == numbers_average:
            on_average = on_average + 1

    print ("\nThe average value of all the values entered is %.1f\n" % (numbers_average))
    print (above_average, "values were above the average\n")
    print (below_average, "values were below the average\n")
    print (on_average, "values were equal to the average\n")


def hi_lo (a_list):
    lowest_number = math.inf
    highest_number = -math.inf

    for number in a_list:
        if lowest_number > number:
            lowest_number = number
        if highest_number < number:
            highest_number = number

    print ("%.1f was the lowest number input\n" % (lowest_number))
    print ("%.1f was the highest number input\n" % (highest_number))


#code

print ("This program will take up to 15 values, iterate them in order and reverse")
print ("order, calculate the average, display how many values were above, below, and")
print ("equal to the average, and output the highest and lowest values entered.\n")


numValues = (input ("How many values would you like to input > ")) 

int_valid = is_int_valid (numValues)
int_range = is_int_in_range (numValues)

while (int_range == False or int_valid == False):
    if int_range == False:
        print ("The value entered is outside the range. Acceptable values are between 1 and 15.")
        numValues = input ("How many values would you like to input > ")
        int_range = is_int_in_range (numValues)
        int_valid = is_int_valid (numValues)

    if int_valid == False:
        print ("The value entered needs to be an integer.")
        numValues = input ("How many values would you like to input > ")
        int_valid = is_int_valid (numValues)
        int_range = is_int_in_range (numValues)

numValues = int (numValues)

user_list = input_nums (numValues)

in_order (user_list)

rev_order (user_list)

abo_bel_equ (user_list, numValues)

hi_lo (user_list)
