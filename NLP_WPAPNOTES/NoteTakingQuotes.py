import fileinput, re, nltk

def recursive_loop(word_list, steps, word, word2=False):   # Adds spaces
    options = [word, word2]
    exceptions = ['.', ',', ' ', '\n', '', '(', ')']
    if word == '"':
        exceptions.append('<')
        exceptions.append('>')
        #exceptions.remove(')') Do this
    if word == '<':
        exceptions.append('"')
    word_list = list(word_list)
    for i, letter in enumerate(word_list):
        if i != len(word_list) - 1:

            if steps == 1:
                if word_list[i + 1] == word: # Add another one of the split just in case
                    steps += 1
                    if letter != ' ' and letter not in exceptions:
                        word_list.insert(i + 1, ' ')
                        original, new = word_list[:i + 3], recursive_loop(word_list[i + 3:], steps, word, word2)
                        final = original + new
                    else:   # If 1st occurenced spaced, but 2nd isn't
                        original, new = word_list[:i + 2], recursive_loop(word_list[i + 2:], steps, word, word2)
                        final = original + new
                    return ''.join(final)

            else:
                if word_list[i + 1] in options and word_list[i + 2] not in exceptions:
                    steps -= 1
                    word_list.insert(i + 2, ' ')
                    soriginal, snew = word_list[:i + 3], recursive_loop(word_list[i + 3:], steps, word, word2)
                    snew = list(snew)
                    sfinal = soriginal + snew
                    return sfinal
                if word_list[i + 1] in options and word_list[i + 2] in exceptions:
                    steps -= 1
                    soriginal, snew = word_list[:i + 2], recursive_loop(word_list[i + 2:], steps, word, word2)
                    snew = list(snew)
                    sfinal = soriginal + snew
                    return sfinal
    return list(word_list)

def rid__(word_list, steps): # Gets rid of the long -
    word_list = list(word_list)
    for i, letter in enumerate(word_list):
        if i != len(word_list) - 1:
            if word_list[i + 1] == '—':
                if steps == 1:
                    word_list.insert(i + 1, '<')
                    word_list.remove('—')
                    steps += 1
                else:
                    word_list.insert(i + 1, '>')
                    word_list.remove('—')
    return ''.join(word_list)

def start_correcting(path):
    with open('{}_all'.format(path), 'r') as f:   # Makes .' or ." seperate sentence
        # Make it so it checks first before doing it
        quote_searcher = re.compile(r'(.*)(\.\"|\.\')(.*)')
        for line in f:
            occurs = quote_searcher.search(line)
            if occurs != None:
                if occurs.group(3) != '\n' and occurs.group(3) != '':
                    with fileinput.FileInput('{}_all'.format(path), True) as fs:
                        for sline in fs:
                            print(sline.replace
                            (line, (occurs.group(1) +
                                    occurs.group(2) +
                                    '\n' +
                                    occurs.group(3) +
                                    '\n')), end='')

    with open('{}_all'.format(path), 'r') as f:
        quote_searcher = re.compile(r'—+')
        for line in f:
            occurs = quote_searcher.search(line)
            if occurs != None:
                final_sentence = rid__(line, 1)
                with fileinput.FileInput('{}_all'.format(path), True) as fs:
                    for sline in fs:
                        print(sline.replace(line, final_sentence), end='')

    with open('{}_all'.format(path), 'r') as f:   # Adds spaces to '"'
        quote_searcher = re.compile(r'(\".*\")')
        for line in f:
            occurs = quote_searcher.search(line)
            if occurs != None:
                final_sentence = recursive_loop(line, 1, '"')
                with fileinput.FileInput('{}_all'.format(path), True) as fs:
                    for sline in fs:
                        print(sline.replace(line, final_sentence), end='')

    with open('{}_all'.format(path), 'r') as f:   # Adds spaces to '"'
        quote_searcher = re.compile(r'(\'.*\')')
        for line in f:
            occurs = quote_searcher.search(line)
            if occurs != None:
                if occurs.group(1)[1] == 's':
                    continue
                final_sentence = recursive_loop(line, 1, '\'')
                with fileinput.FileInput('{}_all'.format(path), True) as fs:
                    for sline in fs:
                        print(sline.replace(line, final_sentence), end='')

    with open('{}_all'.format(path), 'r') as f:   # Adds spaces to < and >
        quote_searcher = re.compile(r'(<.*>)|(<.*)')
        for line in f:
            occurs = quote_searcher.search(line)
            if occurs != None:
                final_sentence = recursive_loop(line, 1, '<', '>')
                with fileinput.FileInput('{}_all'.format(path), True) as fs:
                    for sline in fs:
                        print(sline.replace(line, final_sentence), end='')
