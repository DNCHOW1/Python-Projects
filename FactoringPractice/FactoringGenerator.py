import random, re

def rid_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

def standard(term1, term2):
    all_terms = []
    new_terms = []
    future_combo = ''
    for num in term1:
        for numv2 in term2:
            product_ = num[0] * numv2[0]

            if str(num[1])[:2] == str(numv2[1])[:2] and str(num[1])[0].isalpha(): # Both of them have same variable term
                all_terms.append([str(product_), (num[1][0] + '^{}'.format(int(num[1][-1]) + int(numv2[1][-1])))])

            elif str(num[1])[0].isalpha() or str(numv2[1])[0].isalpha():    # One of them has variable term
                try:
                    if str(num[1])[-2] == str(numv2[1])[-2]:
                        combination = str(num[1][0]) + str(numv2[1][0]) # If there are multiple terms
                        if future_combo == '':
                            future_combo = combination
                        if combination[::-1] == future_combo or combination == future_combo:    # Needs improvement
                            all_terms.append([str(product_), future_combo + '^' + '1'])
                            continue
                except:
                    if num[1] != 1: # Checks to see which one has variable
                        all_terms.append([str(product_), str(num[1])])
                        continue
                all_terms.append([str(product_), str(numv2[1])])

            else:   # If both of them are just whole numbers
                all_terms.append([str(product_), '1'])

    variable_terms = [second for first, second in all_terms]
    variable_terms = rid_duplicates(variable_terms) # All the variables in above terms
    for variables in variable_terms: # Will add up variables that are the same
        product_2 = 0
        for first, second in all_terms:
            if variables == second:
                product_2 += int(first)
        if variables == '1':
            new_terms.append(str(product_2))
            continue
        new_terms.append(str(product_2) + variables)

    marked = []
    for i, v in enumerate(new_terms):
        if v[0] == '0':
            marked.append(v)
    for i in marked:
        new_terms.remove(i)
    return new_terms

def back_to_form(term): # Makes the resulting equation go back into form seen below
    try:
        letter = term[0][-3] # Add a try and except function?
    except:
        letter = term[0][1][0]
        for i, v in enumerate(term):
            if v[1] != 1:
                term[i] = str(v[0]) + v[1]
            else:
                term[i] = str(v[0])
    letter_regex = re.compile(r'(.*){}(.*)'.format(letter))
    for i, v in enumerate(term):
        mo = letter_regex.search(v)
        if mo != None:
            term[i] = [int(mo.group(1)), letter + mo.group(2)] # Gets it into the form seen below
            continue
        term[i] = [int(v), 1] # If its a whole number, with no variable

def common_factor(factor, term1, term2=0):
    multiplied_term = term1
    if term2 != 0:
        multiplied_term = standard(term1, term2)
    back_to_form(multiplied_term)
    final_term = standard(factor, multiplied_term)
    return final_term

#answer = standard([[1, 'x^1'], [-3, 1]], [[1, 'x^1'], [-2, 1]])
#answer = standard([[1, 'y^1'], [-3, 'z^1']], [[7, 'y^1'], [-4, 'z^1']]) # Problem
#answer = standard([[2, 'b^1'], [5, 'd^1']], [[2, 'a^1'], [-3, 'c^1']]) # Problem
#answer = standard([[50, 'w^1'], [-33, 'v^1']], [[2, 'w^1'], [-3, 'v^1']])
#answer = standard([[1, 'x^1'], [2, 1]], [[1, 'x^1'], [-2, 1]]) # A square function
#answer = standard([[1, 'x^1'], [2, 1]], [[1, 'x^2'], [-2, 'x^1'], [4, 1]]) # A cubic function
#answer = standard([[1, 'y^4'], [-5, 1]], [[1, 'y^8'], [5, 'y^4'], [25, 1]]) # A big function
#answer = common_factor([[2, 'c^1']], [[4, 'c^1'], [-5, 1]], [[1, 'c^1'], [-3, 1]])
#answer = common_factor([[5, 1]], [[6, 'q^1'], [7, 1]], [[6, 'q^1'], [7, 1]])
#answer = common_factor([[1, 'x^1'], [3, 1]], [[1, 'x^1'], [-3, 1]], [[1, 'x^1'], [-5, 1]])
