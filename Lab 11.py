'''
CIS 231 Lab 11
Ashley Bruce and Sky Urman
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


my_dictionary = histogram ("computer")
one_computer = reverse_lookup (my_dictionary, 1)
print (one_computer)
two_computer = reverse_lookup (my_dictionary, 2)
print (two_computer)


print (factorial (1))
print (factorial (2))
print (factorial (3))
print (factorial (4))
print (factorial (5))
print (factorial (6))
print (factorial (7))
print (factorial (8))
print (factorial (9))
print (factorial (10))

