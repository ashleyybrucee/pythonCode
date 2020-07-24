'''
CIS 231 Lab 8
Ashley Bruce
09-11-19
'''

# part 1

def char_in_word (char, word):
    i = 0
    count = 0

    while i < len (word):
        if char == word [i]:
            count = count + 1
        i = i + 1

    if count > 0:
        return count
    else:
        return 0


# part 2

def char_removed (char, word):
    l = len (word)
    new_string = ""

    for i in range (l):
        if char != word [i]:
            new_string = new_string + word[i]

    return new_string

# part 3

def all_possible_slices (string):
    slice_start = 0

    for char in string:
        slice_end = slice_start
    
        for i in range (slice_start + 1, len(string) + 1):
            slice_end = slice_end + 1
            print (slice_start, slice_end, string [slice_start:slice_end])
           

        slice_start = slice_start +1


#test cases

print ("The letter a appears", char_in_word ("a", "banana"), "times in banana")
print ("The letter c appears", char_in_word ("c", "happy"), "times in happy")
print ("The letter b appears", char_in_word ("b", "bubbly"), "times in bubbly")
print ("\n")

print ("rabbit with 'b' removed is", char_removed ("b", "rabbit"))
print ("vegetables with 'e' removed is", char_removed ("e", "vegetables"))
print ("bubbly with 'b' removed is", char_removed ("b", "bubbly"))
print ("\n")

print ("This will give you every possible slice of a string")
user_string = input ("Input your string > ")
all_possible_slices (user_string)
user_string = input ("Input your string > ")
all_possible_slices (user_string)
user_string = input ("Input your string > ")
all_possible_slices (user_string)
