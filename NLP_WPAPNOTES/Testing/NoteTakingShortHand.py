import pyperclip, random
text = pyperclip.paste()
# For accurate results, use 1st page of Chapter 17 Lesson 1
# Text will be originally 1806 letters
# Unable to determine important words, so omits vowels of people!
vowels = ['a', 'e', 'i', 'o', 'u']
test_text = '''For almost a thousand years, most Europeans had remained in their small region of the world'''

#test_text = nltk.word_tokenize(test_text)
# removed_vowels = ''.join([word for word in text if word not in vowels]) 1258 letters

def probability_spin():
    number = random.randint(0, 4)
    if number == 5:
        return True
    else:
        return False

def removeVowels(text):
    approved_words = []
    #for i in range(10):
    exceptions = ['.', ' ', '?']
    for pos, letter in enumerate(text): # 1328 letters w/o probability_spin
        if letter not in vowels:
            approved_words.append(letter)
        elif text[pos - 1] in exceptions:
            approved_words.append(letter)
        elif probability_spin():
            approved_words.append(letter)
        else:
            pass
    return approved_words
'''
removed_vowels = ''.join(approved_words)        Debugging
print('\n')
print(removed_vowels)
print('\n--------------------------\n')
approved_words = []'''

# If real_min and max are closer, results are better

# Probability - min/max (Keep in mind, probability increase chance of adding vowel)
# 1/6 prob - 1387/1425 - Surprisingly readable, annoying that it omits some names
# 1/5 prob - 1405/1441
# 1/4 prob - 1428/1472 - Increased vowels throw off flow of sentence, makes pronouncing hard
# 1/3 prob - 1461/1513
# 1/2 prob - 1500/1601 - Extremely legible, probably best along with other methods
