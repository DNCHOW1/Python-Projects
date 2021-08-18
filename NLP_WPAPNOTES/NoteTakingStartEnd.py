import fileinput, re, nltk, NoteTakingSplitter

full_sentences = []
starting = []
ending = []
diff_combined = ['good_combined', 'bad_combined']
chapter = 'Chapter_2'
with open('{}/Lesson4_all'.format(chapter), 'r') as f:
    for sentence in f:
        full_sentences.append(sentence)

for i, sentence in enumerate(full_sentences):
    if i != 0 and i != len(full_sentences) - 1:
        if full_sentences[i - 1] == '^\n':
            starting.append(sentence)
        if full_sentences[i + 1] == '^\n':
            ending.append(sentence)

for combined in diff_combined:
    for i, parent_sentence in enumerate(starting):
        sentence_searcher = re.compile(r'(.*)(\n$)')
        with open('{}/{}'.format(chapter, combined), 'r') as f:
            for line in f:
                if line == parent_sentence:
                    mo = sentence_searcher.search(line)
                    if mo != None:
                        new_line = mo.group(1) + ' ' + '$' + mo.group(2)
                        with fileinput.FileInput('{}/{}'.format(chapter, combined), True) as fs:
                            for sline in fs:
                                print(sline.replace(line, new_line), end='')

    for i, parent_sentence in enumerate(ending):
        sentence_searcher = re.compile(r'(.*)(\n$)')
        with open('{}/{}'.format(chapter, combined), 'r') as f:
            for line in f:
                if line == parent_sentence:
                    mo = sentence_searcher.search(line)
                    if mo != None:
                        new_line = mo.group(1) + ' ' + '@' + mo.group(2)
                        with fileinput.FileInput('{}/{}'.format(chapter, combined), True) as fs:
                            for sline in fs:
                                print(sline.replace(line, new_line), end='')
