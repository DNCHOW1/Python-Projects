import nltk, pyperclip
from nltk.corpus import wordnet
from nltk.stem.wordnet import WordNetLemmatizer
#test_text = 'For almost a thousand years, most Europeans had remained in their small region of the world. Then, between 1500 and 1800, European explorers used improved sailing ships to travel and explore the rest of the world. First Portugal and Spain, and then later the Netherlands, England, and France, reached to new economic heights through their travels and resulting trading activity. At the end of the fifteenth century, they set out on a remarkable series of overseas journeys. What caused them to undertake such dangerous voyages? '

test_text = pyperclip.paste()

exceptions = [',', '.', '?']

tokens = nltk.word_tokenize(test_text)
tagged = nltk.pos_tag(tokens)
lemmatizer = WordNetLemmatizer()
def get_pos_tag(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

for i, word in enumerate(tagged):   # Getting rid of plural stuff(lemmatize)
    if get_pos_tag(word[1]) != '':
        new_word = lemmatizer.lemmatize(word[0], get_pos_tag(word[1]))
        tokens[i] = new_word
    else:
        continue

for i, word in enumerate(tokens):   # Uses good spacing
    if i != (len(tokens) - 1):
        if tokens[i + 1] not in exceptions and word != ' ' and word != '“':
            tokens.insert(i + 1, ' ')

new_sentence = ''.join(tokens)
print(len(new_sentence), len(test_text))
#word = lemmatizer.lemmatize('going', wordnet.VERB)
