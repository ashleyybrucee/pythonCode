# Ashley Bruce
# Lab 5
# CIS 231
# 8-28-19

x_string = input ("Please enter a value between 0 and 59 for x: ")
x = int (x_string)

def x_even_or_odd (x):
    if x % 2 == 0:
        print (x, "is an even number. \n")
    else:
        print (x, "is an odd number. \n")

x_even_or_odd (x)

def x_in_minutes (x):
    print ("If x is a value in minutes, it would be:")
    if 0 <= x <= 30:
        print (x, "minutes after the hour. \n")
    else:
        print (60-x, "minutes before the hour. \n")

x_in_minutes (x)

y_string = input ("Please enter a value for y: ")
y = int (y_string)

def compare_x_and_y (x, y):
    print ("The values you have entered for x and y are", x, "and", y, "respectively.")
    if x > y:
        print ("x > y")
    elif x < y:
        print ("x < y")
    else:
        print ("x == y")

compare_x_and_y (x,y)
