import nltk, pyperclip
from nltk.corpus import names

with open('Chapter_2/good_combined', 'r') as f:
    good_sentences = [nltk.word_tokenize(line) for line in f if line != '^\n'
                                               if line != '*empty*\n']

with open('Chapter_2/bad_combined', 'r') as f:
    bad_sentences = [nltk.word_tokenize(line) for line in f if line != '^\n'
                                               if line != '*empty*\n']

all_names = [name for name in names.words('male.txt')] + [name for name in names.words('female.txt')]

g, b = 0,0
for i in good_sentences:
    for word in i:
        if word in all_names:
            #print(i)
            #print(word)
            #print(nltk.pos_tag(i))
            g += 1

for i in bad_sentences:
    for word in i:
        if word in all_names:
            print(i)
            print(word)
            print(nltk.pos_tag(i))
            b += 1

print(g)
print(b)













'''good_sentences = good_sentences[:88]
bad_sentences = bad_sentences[:88]
all_sentences = good_sentences + bad_sentences

all_words = [word for sentence in all_sentences for word in sentence]
f_dist = FreqDist()

for i in all_words:
    f_dist[i] += 1
good_score, bad_score = 0, 0
for i in good_sentences:
    temp_score = 0
    for word in i:
        temp_score += f_dist[word]
    good_score += temp_score / len(i)

for i in bad_sentences:
    temp_score = 0
    for word in i:
        temp_score += f_dist[word]
    bad_score += temp_score / len(i)

print(good_score)
print(bad_score)'''
