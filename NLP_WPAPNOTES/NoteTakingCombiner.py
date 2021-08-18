good_sentences, bad_sentences = [], []

def start_bad(path):
    with open('{}_good'.format(path), 'r') as f:
        for line in f:
            if line != '^\n' and line != '*empty*\n':
                good_sentences.append(line)

    with open('{}_all'.format(path), 'r') as f:
        with open('{}_bad'.format(path), 'w') as bf:
            for i, line in enumerate(f):
                if line == '^\n' or line not in good_sentences:
                    bad_sentences.append(line)

            for i, sentence in enumerate(bad_sentences):
                if sentence == '^\n' and bad_sentences[i - 1] == '^\n':
                    bad_sentences.insert(i, '*empty*\n')

            for sentences in bad_sentences:
                bf.write(sentences)

def start_good(path):
    with open('{}_bad'.format(path), 'r') as f:
        for line in f:
            if line != '^\n' and line != '*empty*\n':
                bad_sentences.append(line)

    with open('{}_all'.format(path), 'r') as f:
        with open('{}_good'.format(path), 'w') as gf:
            for i, line in enumerate(f):
                if line == '^\n' or line not in bad_sentences:
                    good_sentences.append(line)

            for i, sentence in enumerate(good_sentences):
                if sentence == '^\n' and good_sentences[i - 1] == '^\n':
                    good_sentences.insert(i, '*empty*\n')

            for sentences in good_sentences:
                gf.write(sentences)
