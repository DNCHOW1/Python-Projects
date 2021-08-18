import Assignments
class GradeType:
    def __init__(self, subject, wHW, wQUIZ, wTEST):
        self.subject = subject
        self.wHW = wHW
        self.wQUIZ = wQUIZ
        self.wTEST = wTEST
        self.HW = {}
        self.QUIZ = {}
        self.TEST = {}

    def hwGrade(self):
        if len(self.HW) != 0:
            x = 0
            for grades in self.HW.values():
                x += grades
            x = x / len(self.HW)
            return x
        else:
            return 0

    def quizGrade(self):
        if len(self.QUIZ) != 0:
            x = 0
            for grades in self.QUIZ.values():
                x += grades
            x = x / len(self.QUIZ)
            return x
        else:
            return 0

    def testGrade(self):
        if len(self.TEST) != 0:
            x = 0
            for grades in self.TEST.values():
                x += grades
            x = x / len(self.TEST)
            return x
        else:
            return 0

    def checkWeights(self, hw, quiz, test):
        if len(self.HW) == 0:
            hw = 0
        if len(self.QUIZ) == 0:
            quiz = 0
        if len(self.TEST) == 0:
            test = 0
        return hw, quiz, test

    def totalGrade(self, hw, quiz, test):   # Gets total grade of the class
        tempHW, tempQUIZ, tempTEST = self.checkWeights(self.wHW, self.wQUIZ ,self.wTEST)
        total_weight = tempHW + tempQUIZ + tempTEST
        total = hw * self.wHW + quiz * self.wQUIZ + test * self.wTEST
        total = (total / total_weight)
        return total

WPAP = GradeType('World History PreAP', .10, .30, .60)  # Just makes the
ENG = GradeType('English II PreAP', .10, .30, .60)      # classes with their
ALG = GradeType('Algebra II PreAp', .10, .30, .60)      # specific weights for
CHEM = GradeType('Chemistry PreAP', .10, .30, .60)      # each grade
SPAN = GradeType('Spanish I', .15, .30, .55)
PROF = GradeType('Prof. Communications', .15, .35, .50)
PE = GradeType('Physical Education', 0, 0, 1)

all_classes = [WPAP, ENG, ALG, CHEM, SPAN, PROF, PE]

def addAssignment(split_portion, subject):
    for i in range(len(all_classes)):
        if subject == Assignments.all_subjects[i]:
            if split_portion[2] == 'Hw':    # Adds the assignment and it's grade into specific types
                all_classes[i].HW[split_portion[0]] = int(split_portion[1])
            if split_portion[2] == 'Quiz':
                all_classes[i].QUIZ[split_portion[0]] = int(split_portion[1])
            if split_portion[2] == 'Test':
                all_classes[i].TEST[split_portion[0]] = int(split_portion[1])
        else:
            pass

def finalGrade(iteration):  # Gets grade of the class, and rounds it
    final_grade = all_classes[iteration].totalGrade(all_classes[iteration].hwGrade(),
                                                    all_classes[iteration].quizGrade(),
                                                    all_classes[iteration].testGrade())
    final_grade = round(final_grade, 2)
    return final_grade

def printAllClassAverages():
    for i in range(len(all_classes)):
        final_grade = str(finalGrade(i))    # So that it can ben r.justed
        len_adjust = 27 - len(all_classes[i].subject) # So that it looks neat
        print('{}{} '.format(all_classes[i].subject, final_grade.rjust(len_adjust, '.')))

def timeStamp():
    temp_list = []      # 2 lists that contain b_and_a
    for i in range(len(all_classes)):   # Before
        final_grade = finalGrade(i)
        temp_list.append(final_grade)
    return temp_list

def before_and_after():
    before = timeStamp()
    Assignments.readPaths() # Updates the paths
    after = timeStamp()
    print_b_and_a(before, after)

def print_b_and_a(before, after): # 24, 7
    special_str = 'Before:'.rjust(29), 'After:'.rjust(7) # Adjusts accordingly
    print(special_str[0] + special_str[1])
    for i in range(len(all_classes)):
        len_adjust = 27 - len(all_classes[i].subject)   # So it looks neat with the rows
        sbefore, safter = str(before[i]), str(after[i])
        print('{}{}/{}'.format(all_classes[i].subject, sbefore.rjust(len_adjust, '.'),
                                                       safter.rjust(7, '.')))

def removeAssignments(grade_type, position):  # Removes assignment the dict, so no affect grades
    if grade_type[2] == 'Hw':
        all_classes[position].HW.pop(grade_type[0])
    if grade_type[2] == 'Quiz':
        all_classes[position].QUIZ.pop(grade_type[0])
    if grade_type[2] == 'Test':
        all_classes[position].TEST.pop(grade_type[0])
