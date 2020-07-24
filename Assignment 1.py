'''
CIS 231 Assignment 1
Ashley Bruce
09-07-19
'''

def farenheit_to_celsius ():
    degrees_farenheit = float (input ("Please enter a temperature in degrees Farenheit > "))
    degrees_celsius = (degrees_farenheit - 32.0) * 5.0 / 9.0
    return degrees_farenheit, degrees_celsius
    print ("\n")


print ("This program converts 5 values in degrees Farenheit to degrees Celsius \n")

farenheit_one, celsius_one = farenheit_to_celsius ()
farenheit_two, celsius_two = farenheit_to_celsius ()
farenheit_three, celsius_three = farenheit_to_celsius ()
farenheit_four, celsius_four = farenheit_to_celsius ()
farenheit_five, celsius_five = farenheit_to_celsius ()

farenheit_sum = farenheit_one + farenheit_two + farenheit_three + farenheit_four + farenheit_five
celsius_sum = celsius_one + celsius_two + celsius_three + celsius_four + celsius_five

farenheit_average = farenheit_sum / 5
celsius_average = celsius_sum / 5

print ("\nThe 5 temperatures you have entered in degrees Farenheit are:")
print ("%.2f, %.2f, %.2f, %.2f, %.2f \n" % (farenheit_one, farenheit_two, farenheit_three, farenheit_four, farenheit_five))
print ("The total value of all the Farenheit temperatures is %.2f" % (farenheit_sum))
print ("The average value of all the Farenheit temperatures is %.2f \n" % (farenheit_average))

print ("Here are the conversions to Celcius for the values you input: \n")
print (" %.2f degrees Farenheit = %.2f degrees Celsius" % (farenheit_one, celsius_one))
print (" %.2f degrees Farenheit = %.2f degrees Celsius" % (farenheit_two, celsius_two))
print (" %.2f degrees Farenheit = %.2f degrees Celsius" % (farenheit_three, celsius_three))
print (" %.2f degrees Farenheit = %.2f degrees Celsius" % (farenheit_four, celsius_four))
print (" %.2f degrees Farenheit = %.2f degrees Celsius \n" % (farenheit_five, celsius_five))

print ("The 5 temperatures you have entered converted to degrees Celsius are:")
print ("%.2f, %.2f, %.2f, %.2f, %.2f \n" % (celsius_one, celsius_two, celsius_three, celsius_four, celsius_five))
print ("The total value of all the Celsius temperatures is %.2f" % (celsius_sum))
print ("The average value of all the Celsius temperatures is %.2f" % (celsius_average))



