'''
CIS 231 Lab 9
Ashley Bruce
09-12-19
'''


print ("This program will take 15 values, iterate them in order and reverse order")
print ("calculate the average, display how many values were above, below, and")
print ("equal to the average, and output the highest and lowest values entered.")

print ("\nPlease enter 15 values, one at a time, as you are prompted to.")

my_list = []
sum_numbers = 0
below_average = 0
above_average = 0
on_average = 0

user_number = float (input ("Please input your first value > "))
my_list.append (user_number)
sum_numbers = sum_numbers + user_number
high_number = user_number
low_number = user_number

for i in range (14):
    user_number = float (input ("Please enter a value > "))
    my_list.append (user_number)
    sum_numbers = sum_numbers + user_number
    if high_number < user_number:
        high_number = user_number
    if low_number > user_number:
        low_number = user_number

numbers_average = sum_numbers / 15

for number in my_list:
    if number > numbers_average:
        above_average = above_average + 1
    if number < numbers_average:
        below_average = below_average + 1
    if number == numbers_average:
        on_average = on_average + 1

print ("\nHere all the values you input in order:")
for number in my_list:
    print (number)

print ("\nHere are the values you input in reverse order:")
for number in my_list [::-1]:
    print (number)

print ("\nThe average value of all the values entered is %.1f" % (numbers_average))

print ("\n", above_average, "values were above the average")

print ("\n", below_average, "values were below the average")

print ("\n", on_average, "values were equal to the average")

print ("\nThe highest number input was", high_number)

print ("\nThe lowest number input was", low_number)
