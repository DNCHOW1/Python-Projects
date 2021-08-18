import re, pyperclip, random

searchWord = pyperclip.paste()  # Remember that this copies stuff
#searchWord = 'Cats crabs dabs sabs Bats bad Ads'
def randomWord(text):
    words = text.split()
    number_of_words = len(words) - 1
    while True:
        chosenWord = random.randint(0, number_of_words)
        chosenWord = words[chosenWord]
        if len(chosenWord) >= 4:
            condition = chosenWord.isalpha()
            if condition == True:
                break
            else:
                chosenWord = list(chosenWord)
                for letter in range(len(chosenWord)):
                    word = chosenWord[letter]
                    anotherCondition = word.isalpha()
                    if anotherCondition == True:
                        continue
                    else:
                        chosenWord[letter] = '1'
                chosenWord = getRidOfOnes(chosenWord)
                chosenWord = ''.join(chosenWord)
                break
        else:
            continue
    return chosenWord

def getRidOfOnes(word1):
    number_of_1s = 0
    for i in word1:
        if i.isdecimal() == True:
            number_of_1s += 1
        else:
            continue

    for i in range(number_of_1s):
        occurence = word1.index('1')
        word1.pop(occurence)
    return word1

def end_of_word(word):
    word = word[-3:]
    return word

def searchAllEnds(paragraph, ending):
    # NOTE:Make it so if there's something after the end, prints it too
    endingWords = re.compile(r'\S+?{}'.format(ending))
    print(endingWords.findall(paragraph))

def start():
    chosenWord = randomWord(searchWord)
    wordEnd = end_of_word(chosenWord)
    print(chosenWord, wordEnd)
    searchAllEnds(searchWord, wordEnd)

start()
