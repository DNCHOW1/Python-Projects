import re, pyperclip, nltk, GoodSpace
from nltk.corpus import stopwords
# implement synonyms that make these sentences shorter

# Maybe make algorithm that summarizes text using the tagged words! Subtract the
# score from the len of the sentence or something bc then it would favor long sentences
# Make it so that the space adder is more accurate
exceptions = ['not']
def replace_words(sentence_list):
    exceptions = [',', '.', '?']
    tokens = nltk.word_tokenize(sentence_list)
    for i,v in enumerate(tokens):
        if v == 'and':      # Make a dictionary with all the keys and values
            tokens[i] = '&'
        elif v == 'in':
            tokens[i] = '>'
        elif v == 'as':
            tokens[i] = '-'
        elif v == 'with':
            tokens[i] = 'w/'
    tokens = GoodSpace.good_spacing(tokens)
    return tokens

def manual_continue(sentence):  # For manual summarization
    print(sentence)
    user_response = input('Press enter to confirm sentence:\n')
    if user_response == '':
        return True
    else:
        return False

def remove_stopwords(paragraph):
    stopWords = set(stopwords.words('english'))
    tokens = nltk.word_tokenize(paragraph)
    for words in tokens:
        if words.lower() in stopWords:
            if words.lower() != 'and':
                if words.lower() not in exceptions:
                    tokens.remove(words)
    return tokens

def get_rid_useless(paragraph):
    tokens = nltk.word_tokenize(paragraph)
    tagged = nltk.pos_tag(tokens)
    for i, word in enumerate(tagged):   # word[1] would be the tag, word[0] being the word
        if word[1] == 'RB' or word[1] == 'RBR' or word[1] == 'RBS' or word[1] == 'WRB':
            if word[0] != 'later':
                tokens.remove(word[0])
        elif word[1] == 'DT':
            tokens.remove(word[0])
    return tokens

def split_into_sentences(text, sentences):
    x = []
    for i in text:
        if i != '.' and i != '?' and i != '!':
            x.append(i)
            continue
        sentence = GoodSpace.good_spacing(x)
        sentence = sentence + i
        print(sentence)
        # if manual_continue(sentence):   # For manual summarization
        sentences.append(sentence)
        x = []
    print('\n')

def start_remove():
    text = pyperclip.paste()
    approved_sentences = []
    paragraph_split = text.split('\n')
    list_of_removers = ['remove_stopwords(shortened_sentence)', 'get_rid_useless(shortened_sentence)']
    for j in range(len(list_of_removers)):
        for i in paragraph_split:
            if i != '':
                shortened_sentence = replace_words(i)
                shortened_sentence = eval(list_of_removers[j])
                split_into_sentences(shortened_sentence, approved_sentences)
            approved_sentences.append('\n')

        final_sentence = GoodSpace.good_spacing(approved_sentences)
        paragraph_split = final_sentence.split('\n')
        approved_sentences = []
    return final_sentence, text

sentence, text = start_remove()

print('\n\n\n\n\n', text, '\n\n\n\n\n')
print(sentence)
print(len(sentence), len(text))
print('\n\n\n\n')
#print('\n\n\n\n\n', text, '\n\n\n\n\n')
#print(r_stop_sentence)
