'''
CIS 231 Assignment 2
Ashley Bruce
Cuesta College - Randy Scovil 
10-17-19
'''

import math

def amount_of_temp_inputs ():
    print ("This program can take up to 35 temperature values in Fahrenheit \nto convert to Celsius.")
    num_input = int (input ("Please input the amount of temperatures you would like to enter: "))

    while (num_input < 1) or (num_input > 35):
        print ("That value is out of range. Valid numbers are between 1 and 35.")
        num_input = int (input ("Please input the amount of temperatures you would like to enter: "))
        
    return num_input


def user_temperatures (num_temps):
    print ("Please enter the", num_temps, "Fahreheit temperatures one at a time.")
    print ("Acceptable values are between -150.0 and 350.0 degrees Fahrenheit.")
    temp_list = []
    
    for temp in range (num_temps):
        temp_fahr = float (input ("Please enter a value in degrees Fahrenheit: "))
        
        while (temp_fahr < -150.0) or (temp_fahr > 350.0):
            print ("The value entered is out of range. Valid temperatures are between \n-150.0 and 300.0.")
            temp_fahr = float (input ("Please enter a value in degrees Fahrenheit: "))
            
        temp_list.append (temp_fahr)
    return temp_list


def selection_sort (list):
    for i in range (len (list) -1):
        min_index = i

        for j in range (i+1, len(list)):
            if list[j] < list [min_index]:
                min_index = j
                
        temp = list[min_index]
        list[min_index] = list[i]
        list[i] = temp


def convert_to_celsius (fahrenheit):
    return ((fahrenheit - 32.0) * 5.0 / 9.0)


def print_f_and_c (fahr_list):
    for fahr in fahr_list:
        print ("\t\t\t %6.1f \t %6.1f" % (fahr, convert_to_celsius(fahr)))


def average_value_of_list (a_list):
    number_sum = 0
    for value in a_list:
        number_sum = number_sum + value
    return (number_sum / len (a_list))


def abo_bel_equ (a_list):
    numbers_average = average_value_of_list (a_list)
    below_average = 0
    above_average = 0
    on_average = 0

    for number in a_list:
        if number > numbers_average:
            above_average = above_average + 1
        elif number < numbers_average:
            below_average = below_average + 1
        else:
            on_average = on_average + 1
    
    print ("Above Average: \t\t   ", above_average)
    print ("Equal to Average: \t   ", on_average)
    print ("Below Average: \t\t   ", below_average, "\n")


def hi_lo (a_list):
    lowest_number = math.inf
    highest_number = -math.inf

    for number in a_list:
        if lowest_number > number:
            lowest_number = number
        if highest_number < number:
            highest_number = number
            
    print ("High: \t\t\t %6.1f \t %6.1f \n" % (highest_number, convert_to_celsius (highest_number)))
    print ("Low: \t\t\t %6.1f \t %6.1f \n" % (lowest_number, convert_to_celsius (lowest_number)))
    

def standard_deviation (a_list):
    if len(a_list) > 1:
        sd_list = []
        the_sum = 0
        average_value = average_value_of_list (a_list)
        for number in a_list:
            sd_number = abs (number - average_value) **2
            sd_list.append (sd_number)

        for number in sd_list:
            the_sum = the_sum + number
            
        corrected_sd = math.sqrt (the_sum / (len (sd_list) -1))

    else:
        corrected_sd = 0

    print ("Standard Deviation: \t %6.1f" % (corrected_sd))

    
def main ():
    fahr_list = (user_temperatures (amount_of_temp_inputs()))
    selection_sort (fahr_list)

    average_fahr = average_value_of_list (fahr_list)
    average_cels = convert_to_celsius (average_fahr)

    print ("\n CIS 231 - Assignment 2 - Ashley Bruce \n")
    print ("\t\t\t  Fahr \t\t   Cels")
    print ("\t\t\t ======= \t  =======")
    print_f_and_c (fahr_list)      
    print ("\t\t\t ======= \t  =======")
    print ("Average: \t\t %6.1f \t %6.1f \n" % (average_fahr, average_cels)) 
    hi_lo (fahr_list)
    abo_bel_equ (fahr_list)
    standard_deviation (fahr_list)

main ()

