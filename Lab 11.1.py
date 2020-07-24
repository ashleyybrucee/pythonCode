'''
CIS 231 Lab 11
Ashley Bruce
10-02-19
'''

# functions

def histogram (string):
    d = dict ()
    for char in string:
        d[char] = d.get (char, 0) + 1   
    return d


def reverse_lookup (d, v):
    list_of_keys = []
    for k in d:
        if d[k] == v:
            list_of_keys.append (k)
    return list_of_keys


def factorial (key):
    known = {1 : 1}
    if key in known:
        return known [key]
    value = key * factorial (key - 1)
    known [key] = value
    return value
    


#test cases

p = histogram ("parrot")
print (p)
c = histogram ("cheezeit")
print (c)
t = histogram ("tabletop")
print (t)


my_dictionary = dict ()
my_dictionary ["eggs"] = "breakfast food"
my_dictionary ["bacon"] = "breakfast food"
my_dictionary ["toast"] = "breakfast food"
my_dictionary ["soup"] = "dinner food"
my_dictionary ["noodles"] = "dinner food"

breakfast_key = reverse_lookup (my_dictionary, "breakfast food")
print (breakfast_key)

second_dictionary = histogram ("parrot")

lunch_key= reverse_lookup (my_dictionary, "lunch food")
print (lunch_key)

two_parrot = reverse_lookup (second_dictionary, 2)
print (two_parrot)
three_parrot = reverse_lookup (second_dictionary, 3)
print (three_parrot)


print (factorial (10))


