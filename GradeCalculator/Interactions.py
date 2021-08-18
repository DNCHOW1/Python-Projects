import Averages, Assignments, GradesRegex

def prompt():
    print('\nThis program will calculate the grade of all of your classes.')
    print("If you wish to view the changes, type M to go back to main screen.")
    print('Typing any symbols below will give you more information.')
    print('Type > then the subject to see all the specific assignments a class.')
    print('Type + to add an assignment to a class.')
    print('Type - to delete an assignment from a class.')
    print('Type | to edit an assignment in a class.')
    print('Type quit to quit from program.')
    print('\n')

def mainScreen():
    print('Averages for Each Class:')
    Assignments.readPaths()
    Averages.printAllClassAverages()
    print('\n')

def classCondition(condition):  # Checks condition if it's none or false
    if condition == None:   # If none, then ran but was aborted
        pass
    else:   # If false, didn't answer a right class
        print('Enter a class next time\n')
    user_response = eContinue('?')
    return user_response # Does this with continue to avoid printing b_and_a

def eContinue(response):    # Gets the user to manually continue, also gets a response
    while response != '':
        response = input('\nPress Enter to continue.')
    prompt()
    response = input()
    return response#g

def viewPath():
    user_response = input('What class would you like to view?\n')
    if user_response in Assignments.all_subjectsv2:
        Assignments.print_assignments(user_response)
    else:
        print('Enter a class next time\n')

def addPath():
    print('Type abort to abort the action.')
    user_response = input('What class would you like to add to?\n')
    if user_response in Assignments.all_subjectsv2:
        outcome = Assignments.adding_assignments(user_response)
        if outcome != False:    # if false not returned, ran sucessfully
            print('Done')
            return True
        else:
            print('\nAborted.')
            return None
    elif user_response == 'abort':
        print('\nAborted.')
        return None
    else:
        return False

def editPath(): # Kinda follow delPath(), but changing dict keys no actually deleting them
    user_response = input('What class would you like to edit?\n')
    for i in range(len(Assignments.all_subjectsv2)):
        if user_response == Assignments.all_subjectsv2[i]:
            Assignments.print_assignments(user_response)
            user_assignment = input('\nType the assignment name you want to change(BE VERY SPECIFIC!):\n')
            while len(user_assignment) < 4:
                user_assignment = input('\nPlease enter more then 4 char for this to be accurate!\n')
            outcome = GradesRegex.customRegex(user_assignment.title(), i, '|')
            if outcome == False:    # If false, error occured
                print('Next time, enter a valid assignment.\n')
                return None         # So that it doesnt run b_and_a
            elif outcome == None:
                return None
            else:
                print('Grade changed.')
            return True     # return true if no aborted, so that it runs b_and_a
        else:
            pass
    return False # Otherwise, user didn't input valid class

def delPath():
    user_response = input('What class\'s assignment would you like to delete?\n')
    for i in range(len(Assignments.all_subjectsv2)):
        if user_response == Assignments.all_subjectsv2[i]: # Remember, only runs if its ==
            Assignments.print_assignments(user_response)
            user_assignment = input('\nType the assignment name you want to delete(BE VERY SPECIFIC!):\n')
            while len(user_assignment) < 4:
                user_assignment = input('\nPlease enter more then 4 char for this to be accurate!\n')
            outcome = GradesRegex.customRegex(user_assignment.title(), i, '-')
            if outcome != True:
                if outcome == False:
                    print('Next time, enter a valid assignment.\n')
                elif outcome == None:
                    print('\nDeletion aborted.')
                return None
            else:
                print('\nAssignment deleted.')
            return True
        else:
            pass
    return False

paths = ['>', '+', '-', '|', 'M']

def start():
    prompt()
    mainScreen()
    user_response = input()
    while user_response != 'quit':
        if user_response in paths:
            if user_response != 'M':
                print('The classes have abbreivations w, e, a, c, s, pc, and p.')
                if user_response != '>':
                    if user_response == '+':
                        class_condition = addPath()
                        if class_condition != True:
                            user_response = classCondition(class_condition)
                            continue    # Avoids printing b_and_a
                        else:
                            pass
                    elif user_response == '-':  # Special, bc it deletes 1st
                        class_condition = delPath() # so have to run b_and_a
                        if class_condition != True:
                            user_response = classCondition(class_condition)
                            continue
                        else:
                            user_response = eContinue(user_response) # Can't run b_and_a
                            continue            # bc deletion from dict
                    elif user_response == '|':
                        class_condition = editPath()
                        if class_condition != True:
                            user_response = classCondition(class_condition)
                            continue
                        else:
                            pass
                    Averages.before_and_after() # Won't run if they aborted or error
                else:   # If you're viewing, don't need to see before and after
                    viewPath()
                user_response = eContinue(user_response)    # Runs this if it's > | - +
            else:
                mainScreen()
                user_response = eContinue(user_response)
        else:   # User entered something else
            print('\nPlease look at the prompt again.')
            user_response = eContinue(user_response)
