import re, pyperclip

# NOTE: Make it so that if it exceeds 16 char, too much

# This will check multiple different regexes to determine if password is strong
passwordLower = re.compile(r'[a-z]')
passwordHigher = re.compile(r'[A-Z]')
password8 = re.compile(r'.{8,16}')
passwordNum = re.compile(r'\d')

# This will search the above string for regexes above, will return something if there is a match
def checks(sample):
    lower = passwordLower.search(sample)
    higher = passwordHigher.search(sample)
    atLeast8 = password8.search(sample)
    numbers = passwordNum.search(sample)

    # Taking advantage of the match, will return True or False if it's None or not.
    lower = lower == None
    higher = higher == None
    atLeast8 = atLeast8 == None
    numbers = numbers == None
    return lower, higher, atLeast8, numbers

def passwordStrength(check):
    # Keep in mind that checks returns a list of True or False, we'll use that
    check = list(check)
    doublechecks = check.count(False)
    if doublechecks == 4:
        print('Your password is pretty strong!')
        return True

    elif doublechecks == 3:     # If one is True, then password may not be strong.
        print('Your password is good, but it could be better.')
        x = check.index(True)   # Checks where it is in list, list index corresponds with the error
        failed(4 - doublechecks, x) # Iterates over only 1 time, only 1 error.

    elif doublechecks == 2:
        print('Your password is decent, but it could be a lot better.')
        x = check.index(True)
        check[x] = False        # Changes to False, because index gets only 1st occurence
        y = check.index(True)   # And sets another var to the result of the placement of other error
        failed(4 - doublechecks,x, y)   # checking for 2 errors this time

    elif doublechecks == 1:
        print('Your password is bad, you need to add these:')
        x = check.index(True)   # Does the same as above, but slightly more
        check[x] = False
        y = check.index(True)
        check[y] = False
        z = check.index(True)
        failed(4 - doublechecks, x, y, z)

    else:                       # If there were no Trues, then input didn't even have anything
        print('Wow, revise everything.')
        failed(4, 0, 1, 2, 3)

def failed(iteration ,num, num1=4, num2=4, num3=4): # If this was called, then num must have a value
    choices = [num, num1, num2, num3]               # Sets it as a list, to make it easier
    for i in range(iteration):                      # Takes in the iteration, which is amount of total errors
        if 0 in choices:                            # If it's 0, then error must be lowercase
            print('Your password could use a lowercase character.')
            x = choices.index(0)                    # Finds the index
            choices[x] = 4                          # changes it, so it won't be used again

        elif 1 in choices:
            print('Your password could use a uppercase character.')
            x = choices.index(1)                    # if it's 1, uppercase
            choices[x] = 4

        elif 2 in choices:
            print('Your passwords should use at least 8 characters.')
            x = choices.index(2)
            choices[x] = 4

        elif 3 in choices:
            print('Your password could use a number.')
            x = choices.index(3)
            choices[x] = 4

print('This program has you enter a password, it then determines the strength.')
print('If it contains:\n{}\n{}\n{}\n{}'.format(
'- At least 8 Characters'.rjust(25),
'- A Lowercase Character'.rjust(25),
'- A Uppercase Character'.rjust(25),
'- A number'.rjust(12)))
print('Then it\'ll be copied to the clipboard to be used.')
while True:
    user_input = input('Enter a password:\n')
    abc = passwordStrength(checks(user_input))
    if abc == True:
        pyperclip.copy(user_input)
        print('Password has been copied to clipboard.')
        break
    else:
        continue
