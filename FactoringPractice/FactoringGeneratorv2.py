import random, re, FactoringGenerator, DivisorsModule

def create_standard(mode):
    bad_list = [0, 1, -1]
    if mode == 'n': # Normal difficulty
        num1 = random.randint(-10, 10)
        num2 = random.randint(-10, 10)
        while num1 in bad_list or num2 in bad_list:
            num1 = random.randint(-10, 10)
            num2 = random.randint(-10, 10)
    if mode[0] == 'h': # Harder difficulty, with more settings
        while True:
            neg_list = {}
            num1 = random.randint(-20, 20)
            num2 = random.randint(-20, 20)
            if mode[-1] == 'f' or mode[-1] == 's':
                num1 = random.randint(-30, 30)
                num2 = random.randint(-30, 30)

            while num1 in bad_list or num2 in bad_list:   # Makes sure none of the numbers are 0 or 1
                if mode[-1] == 'f' or mode[-1] == 's':  # Special if it's hf or hfs
                    num1 = random.randint(-30, 30)
                    num2 = random.randint(-30, 30)
                else:
                    num1 = random.randint(-20, 20)
                    num2 = random.randint(-20, 20)

            if str(num1)[0] == '-': # Removes integers because they're annoying
                neg_list['num1'] = num1 # They mess up the len thing below
                num1 = int(str(num1)[1:])
            if str(num2)[0] == '-':
                neg_list['num2'] = num2
                num2 = int(str(num2)[1:])

            if len(str(num1)) == 2 or len(str(num2)) == 2:
                if mode[-1] == 'f' or mode[-1] == 's': # If regular hard, just passes
                    d1 = DivisorsModule.match(num1)
                    d2 = DivisorsModule.match(num2)
                    if mode[-1] == 'f': # Hard to factor because so little
                        if len(str(num1)) == 2 and len(str(num2)) == 2:
                            if len(d1) == 1 or len(d2) == 1: # makes sure only 1 factor
                                break
                            else:
                                continue
                        else:
                            continue
                    if mode[-1] == 's': # Hard to factor because so much
                        if len(str(num1)) == 2 and len(str(num2)) == 2:
                            continue
                        else:
                            if len(d1) >= 4 or len(d2) >= 4: # Makes sure it has 4 factors
                                break
                            else:
                                continue
                break
        num1 = neg_list.get('num1', num1)
        num2 = neg_list.get('num2', num2)
    function = [[1, 'x^1'], [num1, 1]], [[1, 'x^1'], [num2, 1]]
    return function

'''s_func = create_standard('n')
answer = FactoringGenerator.standard(s_func[0], s_func[1])
#print(answer, s_func)

s_func = create_standard('h')
answer = FactoringGenerator.standard(s_func[0], s_func[1])
#print(answer, s_func)

s_func = create_standard('hf')
answer = FactoringGenerator.standard(s_func[0], s_func[1])
print(answer, s_func)

s_func = create_standard('hfs')
answer = FactoringGenerator.standard(s_func[0], s_func[1])
print(answer, s_func)'''
