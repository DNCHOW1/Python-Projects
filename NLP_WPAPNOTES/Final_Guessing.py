import pyperclip, GoodSpace, nltk, random, pickle

#TODO: Make it set back to featuresets[:255], and try it

with open('Naive.pickle','rb') as f:   # Will make this run faster
    classifier = pickle.load(f)

with open('LR.pickle','rb') as f:   # Will make this run faster
    LR_classifier = pickle.load(f)

def find_features(document, child_path=0):
    features = {'ADJ': 0, 'VERB': 0, 'NOUN': 0, 'ADV': 0}
    gscore, bscore = 0, 0
    set123 = 0
    tagged = nltk.pos_tag(document) # Using all of them ranks good
    for word, tag in tagged:
        features['contains_{}'.format(word)] = True
        if tag in features:
            features[tag] += 1
        else:
            features[tag] = 1
        if tag.startswith('J'):
            features['ADJ'] += 1
        elif tag.startswith('V'):
            features['VERB'] += 1
        elif tag.startswith('N'):
            features['NOUN'] += 1
        elif tag.startswith('R'):
            features['ADV'] += 1
    features['length'] = len(document)
    features['first_word'] = document[0]
    features['last_word'] = document[-2]
    for i, v in list(features.items()):
        if child_path == 1:
            if i != 'length':
                features.pop(i)
        if child_path == 2:
            if 'contains' not in i:
                if i != 'length':
                    features.pop(i)
        if child_path == 3:
            if i not in ['ADJ', 'ADV', 'NOUN', 'VERB']:
                features.pop(i)
        if child_path == 4:
            if i != 'length':
                if i != 'first_word':
                    if i != 'last_word':
                        features.pop(i)
    return features

all_sentences = {}
all_individual_sentences = []
for parent_iteration in range(5):
    with open('Chapter_2/Testing1_all', 'r') as f:
        guess_list = []
        for line in f:
            if line != '^\n':
                convert_line = nltk.word_tokenize(line)
                label = classifier.classify(find_features(convert_line, parent_iteration + 1))
                if label == 'good':
                    guess_list.append(line)
    all_sentences['sentence_type{}'.format(parent_iteration)] = guess_list

for parent_iteration in range(5):
    with open('Chapter_2/Testing1_all', 'r') as f:
        guess_list = []
        for line in f:
            if line != '^\n':
                convert_line = nltk.word_tokenize(line)
                label = LR_classifier.classify(find_features(convert_line, parent_iteration + 1))
                if label == 'good':
                    guess_list.append(line)
    all_sentences['sentence_type{}'.format(parent_iteration + 5)] = guess_list

for sentences in all_sentences.values():
    #print(len(sentences))
    all_individual_sentences += sentences

true_good, all_list, good_list = [], [], []
weird_score = 0

with open('Chapter_2/Testing1_all', 'r') as f:
    for line in f:
        if line != '^\n':
            all_list.append(line)

for i in all_list:
    if all_individual_sentences.count(i) >= 3:
        true_good.append(i)

with open('Chapter_2/Testing1_good', 'r') as f:
    for line in f:
        if line != '^\n':
            good_list.append(line)
    for i in true_good:
        if i in good_list:
            weird_score += 1

print(len(all_list))
print(len(true_good))
print(round(weird_score / len(good_list), 4))

#with open('Chapter_2/Testing1_testing', 'w') as f:
    #for sentences in true_good:
        #f.write(sentences)
