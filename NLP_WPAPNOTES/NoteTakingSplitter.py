import pyperclip, GoodSpace, nltk

def split_into_sentences(text, sentences):
    def add_sentences(list_of_sentences, current_word):
        sentence = GoodSpace.good_spacing(list_of_sentences)
        sentence = sentence + current_word
        sentences.append(sentence)
    sentence_enders = ['.', '?', '!']
    sentence_exceptions = ['.', '\"', '\'']
    x = []
    for num, i in enumerate(text):
        if num != len(text) - 1:
            if i not in sentence_enders or text[num + 1] in sentence_exceptions:
                x.append(i)
                continue
            add_sentences(x, i)
            x = []
            continue
        add_sentences(x, i)

def change_words(sentence):
    change_words = {'’': '\'','‘': '\'', '“': '"', '”': '"', '``': '"', '\'\'': '"'}
    for i, word in enumerate(sentence):
        condition = change_words.get(sentence[i], False)
        if condition != False:
            sentence[i] = condition

    return sentence

def checkb_c(sentence):
    for i, word in enumerate(sentence):
        if word.lower() == 'b.c' and sentence[i + 1] == '.':
            try:
                if sentence[i + 2].istitle():
                    pass
                else:
                    sentence[i] = sentence[i] + sentence[i + 1]
                    del sentence[i + 1]
            except:
                pass
    return sentence

def start_adding(path):
    text = pyperclip.paste()

    paragraph_split = text.split('\n')
    with open('{}_all'.format(path), 'a') as f:
        f.write('^\n')
    for i in paragraph_split:
        good_sentences = []
        if i != '':
            t_sentence = nltk.word_tokenize(i)
            c_sentence = change_words(t_sentence)
            c_sentence = checkb_c(c_sentence)
            split_into_sentences(c_sentence, good_sentences)
            with open('{}_all'.format(path), 'a') as f:
                for sentences in good_sentences:
                    f.write('{}\n'.format(sentences))
            continue
        with open('{}_all'.format(path), 'a') as f:
            f.write('^\n')
