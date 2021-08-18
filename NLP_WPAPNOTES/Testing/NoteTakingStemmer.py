import nltk, pyperclip, NoteTakingShortHand
from nltk.stem.snowball import SnowballStemmer
#test_text = 'For almost a thousand years, most Europeans had remained in their small region of the world. Then, between 1500 and 1800, European explorers used improved sailing ships to travel and explore the rest of the world. First Portugal and Spain, and then later the Netherlands, England, and France, reached to new economic heights through their travels and resulting trading activity. At the end of the fifteenth century, they set out on a remarkable series of overseas journeys. What caused them to undertake such dangerous voyages? '

test_text = pyperclip.paste()

exceptions = [',', '.', '?']

stemmer = SnowballStemmer('english')
tokens = nltk.word_tokenize(test_text)
for i, word in enumerate(tokens):   # Getting rid of plural(stemming)
    new_word = stemmer.stem(word)
    tokens[i] = new_word

for i, word in enumerate(tokens):   # Uses good spacing
    if i != (len(tokens) - 1):
        if tokens[i + 1] not in exceptions and word != ' ' and word != '“':
            tokens.insert(i + 1, ' ')

new_sentence = ''.join(tokens)
#print(len(new_sentence), len(test_text))

# Stemming vs Lemmatize: (Using Chapter 17, Lesson 1 for WPAP)
# Lemmatize - 1740 char
# Stemming - 1645 char
# Stemming remove more, but just chops off. Lemmatize less, but is cautious.
# NEVER USE SHORTHAND WITH THE STEMMER
