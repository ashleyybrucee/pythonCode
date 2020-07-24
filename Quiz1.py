'''
In class Quiz
Ashley Bruce
'''

def inputStudent ():
    d = dict ()
    firstName =  (input ("Please enter your first name: "))
    if len (firstName) > 15:
        firstName = firstName [:15]
        
    if len (firstName) == 0:
        firstName = ""
    d['First Name'] = firstName

    lastName = (input ("Please enter your last name: "))
    if len (lastName) > 20:
        lastName = lastName [:20]
        
    if len (lastName) == 0:
        lastName = ""
        
    d['Last Name'] = lastName

    major = (input ("What is your major: "))
    if len (major) > 25:
        major = major [:25]
        
    if len (major) == 0:
        major = ""
    d['Major'] = major


    gpa = (input ("What is your GPA: "))
    try:
        gpa = float (gpa)
        while (gpa < 0) or (gpa > 4):
            print ("The number entered is invalid. Please enter a value between 0 and 4")
            gpa = float (input ("What is your gpa: "))
    except ValueError:
        gpa = -1.0

    d['GPA'] = gpa

    return d


def getStudents (max_value):
    studentList = []
    print ("Please input how many students you want to enter, max number is", max_value)
    studentNumber = int (input ("How many students would you like to enter: "))
    while studentNumber < 0 or studentNumber > max_value:
        studentNumber = int (input ("That value is out of range. Please enter an in range value: "))

    for student in range (studentNumber):
        newStudent = inputStudent ()
        studentList.append (newStudent)

    return studentList


def printStudent (student_dictionary):
    
    student_list = []

    for key in student_dictionary:
        student_list.append(student_dictionary[key])
           
    student_string = student_list[0] + " " + student_list [1] + " " + student_list[2] + " " + str (student_list [3])
    print (student_string)


def printStudents (student_list):
    for student_dictionary in student_list:
        printStudent (student_dictionary)


studentList = getStudents (28)
printStudents (studentList)


