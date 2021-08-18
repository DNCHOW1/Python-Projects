import re, Assignments, fileinput, Averages
gradeConverter = re.compile(r'''
    (.*)
    \-
    \s(\d+)\s
    \/
    \s(.*)''', re.VERBOSE)

def customRegex(word, position, path):
    print('\n')
    wordS = re.compile(word)
    with open(Assignments.all_paths[position], 'r') as f:
        for line in f:
            checkAssignment = wordS.search(line)
            if checkAssignment != None:
                print(line)
                if path == '|':
                    outcome = Assignments.editing_assignments(line, position)
                elif path == '-':
                    outcome = Assignments.deleting_assignments(line, position)
                return outcome
        return False
