good_sentences, bad_sentences = [], []

def start_duplicates(path):
    duplicates = 0
    with open('{}_good'.format(path), 'r') as f:
        for line in f:
            if line != '^\n' and line != '*empty*\n':
                good_sentences.append(line[:20])

    with open('{}_bad'.format(path), 'r') as f:
        for line in f:
            if line != '^\n' and line != '*empty*\n':
                bad_sentences.append(line)

    for i in good_sentences:
        if i in bad_sentences:
            duplicates += 1

    return duplicates
