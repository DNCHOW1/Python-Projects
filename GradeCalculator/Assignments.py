import os, GradesRegex, Averages, fileinput
os.chdir('/Users/DienChau/PythonPractice/PersonalProjects/GradeCalculator/Classes')
WPAP_path = os.path.join(os.getcwd(), 'WPAP.txt')       # Makes the directory
ENG_path = os.path.join(os.getcwd(), 'ENG.txt')         # for each of the text
ALG_path = os.path.join(os.getcwd(), 'ALG.txt')         # files to use later
CHEM_path = os.path.join(os.getcwd(), 'CHEM.txt')
SPAN_path = os.path.join(os.getcwd(), 'SPAN.txt')
PROF_path = os.path.join(os.getcwd(), 'PROF.txt')
PE_path = os.path.join(os.getcwd(), 'PE.txt')

all_paths = [WPAP_path, ENG_path, ALG_path,
             CHEM_path, SPAN_path, PROF_path, PE_path]
all_subjects = ['WPAP.txt', 'ENG.txt', 'ALG.txt',
                'CHEM.txt', 'SPAN.txt', 'PROF.txt', 'PE.txt']
all_subjectsv2 = ['w', 'e', 'a', 'c', 's', 'pc', 'p']

def convertGrades(line):
    converted_grades = GradesRegex.gradeConverter.search(line)
    split_up_grades = [converted_grades.group(1),   # Assignment
                       converted_grades.group(2),   # Grade
                       converted_grades.group(3)]   # Grade Type
    return split_up_grades

def readPaths():
    for i in range(len(all_paths)): # Each iteration will from WPAP to PE
        with open(all_paths[i], 'r') as f:
            for line in f:
                split_up_grades = convertGrades(line)
                Averages.addAssignment(split_up_grades, all_subjects[i])

def addToTxt(subject, assignment, grade, grade_type):
    for i in range(len(all_paths)):
        if subject == all_subjectsv2[i]:
            with open(all_paths[i], 'a') as f:
                f.write('{} - {} / {}\n'.format(assignment, grade, grade_type))
            print('\n')
        else:
            pass

def adding_assignments(subject):    # Adds assignments to the text file
    final_response = 'ajdjkad'
    while final_response.lower() != 'y' or final_response.lower() != 'yes':
        try:    # Error only occurs if they enter a str for the grade
            user_assignment = input('Type the assignment name:\n')
            user_grade = int(input('Type the grade for the assignment:\n'))
            if user_grade >= 0 and user_grade <= 100:
                user_type = input('Type the type of grade it is:\n(h, q, or t:)\n')
                user_type = checkGrade(user_type)
                if user_type != False: # Only runs if it returned valid grade type
                    print('{}, {}, {}\n'.format(user_assignment, user_grade, user_type))
                    final_response = input('Is this what you want?\n')
                    if final_response.lower() == 'y' or final_response.lower() == 'yes':
                        addToTxt(subject, user_assignment.title(), user_grade, user_type)
                        return True
                    elif final_response.lower() == 'abort' or final_response.lower() == 'no':
                        return False
                    else:   # if response was something random
                        print('Alright, starting over.')
                else:
                    print('Please type a valid grade type!')
            else:
                print('Please enter a number from 0 - 100.')
        except:
            print('An error occured...\n')
            return False

def editing_assignments(line, position):
    try:
        user_new_grade = int(input('What would you like to change your grade to?\n'))# New function
        while user_new_grade < 0 or user_new_grade > 100:#
            user_new_grade = int(input('Please enter a number between 0 - 100!\n'))#
    except:
        print('An error occured...')
        print('\nNext time, enter a valid grade.')
        return None
    split_up_grades = convertGrades(line)
    split_up_grades[1] = user_new_grade
    new_grade = ('{}- {} / {}\n'.format(split_up_grades[0],
                                        split_up_grades[1],
                                        split_up_grades[2]))
    with fileinput.FileInput(all_paths[position], True) as fs:
        for sline in fs:
            print(sline.replace(line, new_grade), end='')
    return True

def deleting_assignments(line, position):
    user_response = input('Are you sure you want to delete this assignment?\n')
    if user_response.lower() == 'y' or user_response.lower() == 'yes':
        with fileinput.FileInput(all_paths[position], True) as fs:
            for sline in fs:
                print(sline.replace(line, ''), end='')
        split_up_grades = convertGrades(line)
        before = Averages.timeStamp()   # Gets dict of previous grades
        Averages.removeAssignments(split_up_grades, position)   # This
        readPaths()                                 # And this updates to right now
        after = Averages.timeStamp()    # gets updated dict
        Averages.print_b_and_a(before, after)
        return True
    else:
        return None

def checkGrade(grade):
    if grade.lower() == 'h' or grade.lower() == 'Hw':
        return 'Hw'
    elif grade.lower() == 'q' or grade.lower() == 'quiz':
        return 'Quiz'
    elif grade.lower() == 't' or grade.lower() == 'test':
        return 'Test'
    else:
        return False

def print_assignments(subject):
    for i in range(len(all_subjectsv2)):
        if subject == all_subjectsv2[i]:
            print('\n')
            all_assignments = []
            with open(all_paths[i], 'r') as f:
                for line in f:
                    split_up_grades = convertGrades(line)
                    all_assignments.append(split_up_grades)
                pretty_print(all_assignments)
        else:
            pass

def getLargestLength(list_of_assignments):  # gets largest assignment length to use
    greatest_len = 0
    for i in range(len(list_of_assignments)):
        if len(list_of_assignments[i][0]) > greatest_len: # if the len of the assignment...
            greatest_len = len(list_of_assignments[i][0])
        else:
            pass
    return greatest_len

def pretty_print(list_of_assignments):
    greatest_len = getLargestLength(list_of_assignments)
    adj_len = greatest_len + 5 # Grades will be 5 char away from their assignment
    for i in range(len(list_of_assignments)):
        cur_len = len(list_of_assignments[i][0])    # gets length of current assign
        if list_of_assignments[i][2] == 'Hw':   # Just for neat purposes
            print('{}|{}{}'.format('Home',
                                   list_of_assignments[i][0],
                                   list_of_assignments[i][1].rjust(adj_len - cur_len, '.')))
        else:
            print('{}|{}{}'.format(list_of_assignments[i][2],
                                   list_of_assignments[i][0],
                                   list_of_assignments[i][1].rjust(adj_len - cur_len, '.')))
