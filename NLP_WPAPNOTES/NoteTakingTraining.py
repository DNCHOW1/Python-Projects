import pyperclip, GoodSpace, nltk, random, pickle

from nltk.classify.scikitlearn import SklearnClassifier

from nltk.corpus import names
from sklearn.naive_bayes import MultinomialNB, BernoulliNB  # The classifiers
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

full_good, full_bad = [], []
chapter_numbers = ['17', '18']

for i in chapter_numbers:

    with open('Chapter_{}/good_combined'.format(i), 'r') as f:
        good_sentences = [(nltk.word_tokenize(line), 'good') for line in f if line != '^\n'
                                                         if line != '*empty*\n']

    with open('Chapter_{}/bad_combined'.format(i), 'r') as f:
        bad_sentences = [(nltk.word_tokenize(line), 'bad') for line in f if line != '^\n'
                                                       if line != '*empty*\n']
    #random.shuffle(good_sentences)
    #random.shuffle(bad_sentences)
    full_good += good_sentences # Make use of k-splits
    full_bad += bad_sentences

'''all_words = [words.lower() for sentences in full_good
                           #for words in sentences[0]]

all_wordv2 = [words.lower() for sentences in full_bad
                            for words in sentences[0]]'''

print(len(full_good), len(full_bad))
#all_words = all_words + all_wordv2

def new_data():
    all_tokens = full_good + full_bad
    random.shuffle(all_tokens)       # Pickle this tomorrow!!!
    return all_tokens

def start(input_data, path=0):
    def find_features_o(document):
        features = {}
        features['length'] = len(document)
        return features

    featuresets = [(find_features_o(sentence), tag) for (sentence, tag) in input_data]
    training_set, testing_set = featuresets[:170], featuresets[170:]

    classifier = nltk.NaiveBayesClassifier.train(training_set)

    if path == 1:
        print('Naive Bayes Accuracy % - {}'.format(round(nltk.classify.accuracy(classifier, testing_set) * 100, 2)))
        classifier.show_most_informative_features(15)
    return round(nltk.classify.accuracy(classifier, testing_set) * 100, 2)

def start2(input_data, path=0): # Add contains paragraph_start and end
    def find_features(document, child_path=0):
        features = {'ADJ': 0, 'VERB': 0, 'NOUN': 0, 'ADV': 0}
        gscore, bscore = 0, 0
        tagged = nltk.pos_tag(document) # Using all of them ranks good
        def part_speech(tag, path=0):
            pos_def = {'J': 'ADJ', 'V': 'VERB', 'N': 'NOUN', 'R': 'ADV'}
            the_tag = pos_def.get(tag[0], False)
            if the_tag != False:
                features[the_tag] += 1
        for i, (word, tag) in enumerate(tagged):
            features['contains_{}'.format(word)] = True
            if tag in features:
                features[tag] += 1
            else:
                features[tag] = 1
            part_speech(tag)
        features['length'] = len(document)
        features['first_word_tag'] = tagged[0][1]
        features['last_word_tag'] = tagged[-2][1]
        for i, v in list(features.items()):
            if child_path == 1: # Adds 4 words
                if i != 'length':
                    features.pop(i)
            if child_path == 2: # Adds 2 sentences
                if 'contains' not in i:
                    if i != 'length':
                        features.pop(i)
            if child_path == 3: # adds 3 sentences
                if i not in ['ADJ', 'ADV', 'NOUN', 'VERB']:
                    features.pop(i)
            if child_path == 4:
                if i != 'length':
                    if i != 'first_word':
                        if i != 'last_word':
                            features.pop(i)
        return features

    featuresets = [(find_features(sentence), tag) for (sentence, tag) in input_data]
    #print(len(featuresets))
    training_set, testing_set = featuresets[:170], featuresets[170:]
    #print(len(training_set), len(testing_set))

    classifier = nltk.NaiveBayesClassifier.train(training_set)

    if path == 5:
        all_sentences = {}
        all_individual_sentences = []
        for parent_iteration in range(5):
            with open('Chapter_2/Testing2_all', 'r') as f:
                guess_list = []
                for line in f:
                    if line != '^\n':
                        convert_line = nltk.word_tokenize(line)
                        label = classifier.classify(find_features(convert_line, parent_iteration + 1))
                        if label == 'good':
                            guess_list.append(line)
            all_sentences['sentence_type{}'.format(parent_iteration)] = guess_list

        for sentences in all_sentences.values():
            all_individual_sentences += sentences

        #all_individual_sentences = list(set(all_individual_sentences))
        true_good, all_list, good_list, wierd_score = [], [], [], 0

        with open('Chapter_2/Testing2_good', 'r') as f:
            for line in f:
                if line != '^\n':
                    good_list.append(line)

        '''for i in all_individual_sentences:
            if i in good_list:
                wierd_score += 1
        print('Length of all_sentences: {}'.format(len(all_individual_sentences)))
        print('Length of good_list: {}'.format(len(good_list)))
        print(round(wierd_score / len(good_list), 4))'''

        with open('Chapter_2/Testing2_all', 'r') as f:
            for line in f:
                if line != '^\n':
                    all_list.append(line)
        for i in all_list:
            if all_individual_sentences.count(i) >= 2:
                true_good.append(i)

        for i in true_good:
            if i in good_list:
                wierd_score += 1
        print('Length of all_sentences: {}'.format(len(true_good)))
        print('Length of good_list: {}'.format(len(good_list)))
        print(round(wierd_score / len(good_list), 4))

    if path == 3:
        LR_classifier = SklearnClassifier(LogisticRegression())
        LR_classifier.train(training_set)
        final_score = 0

        for iteration in range(2):
            with open('Chapter_2/Testing{}_all'.format(iteration + 1), 'r') as f:
                wierd_score, guess_list, good_list = 0, [], []
                for line in f:
                    if line != '^\n':
                        convert_line = nltk.word_tokenize(line)
                        label = classifier.classify(find_features(convert_line))
                        if label == 'good':
                            guess_list.append(line)
                with open('Chapter_2/Testing{}_good'.format(iteration + 1), 'r') as sf:
                    for line in sf:
                        if line != '^\n':
                            good_list.append(line)
                for i in guess_list:
                    if i in good_list:
                        wierd_score += 1
                print('Good 1:{}'.format(round(wierd_score / len(guess_list), 4)))
                print('Good 2:{}'.format(round(wierd_score / len(good_list), 4)))
                print(len(guess_list), len(good_list))
                final_score += round(wierd_score / len(good_list), 4)
        return final_score / 2

    if path == 4:   # For looking at errors
        errors = []
        for (sentence, tag) in testing_setv2:
            guess = classifier.classify(find_features(sentence))
            if guess != tag:
                errors.append((tag, guess, sentence))
        errors = sorted(errors)
        for right_category, guessed_category, sentence in errors:
            print('correct: {}, guess: {}, sentence: {}\n'.format(right_category, guessed_category, sentence))

    if path == 1:   # For showing informative features
        print('Naive Bayes Accuracy % - {}'.format(round(nltk.classify.accuracy(classifier, testing_set) * 100, 2)))
        classifier.show_most_informative_features(100) # Set to 200

    if path == 2: # For showing individual accuracy
        print('Naive Bayes Accuracy % - {}'.format(round(nltk.classify.accuracy(classifier, testing_set) * 100, 2)))
        all_training(training_set, testing_set)
    return round(nltk.classify.accuracy(classifier, testing_set) * 100, 2)

def all_training(training, testing, path=0, sentence=0):
    LR_classifier = SklearnClassifier(LogisticRegression())
    LR_classifier.train(training)
    print('LR_classifier Accuracy % - {}'.format(round(nltk.classify.accuracy(LR_classifier, testing) * 100, 2)))

    MNB_classifier = SklearnClassifier(MultinomialNB())
    MNB_classifier.train(training)
    print('MNB_classifier Accuracy % - {}'.format(round(nltk.classify.accuracy(MNB_classifier, testing) * 100, 2)))

    BNB_classifier = SklearnClassifier(BernoulliNB())
    BNB_classifier.train(training)
    print('BNB_classifier Accuracy % - {}'.format(round(nltk.classify.accuracy(BNB_classifier, testing) * 100, 2)))

def average_data(path=0):
    deviation = []
    old, new = 0, 0
    for iteration in range(15):
        final_data = [vers_1, vers_2] = [], []
        for i in range(25):
            data = new_data()
            accuracy = start(data)
            if path == 1:
                accuracy = 0
            vers_1.append(accuracy)
            accuracy = start2(data)
            if path == 1:
                accuracy = start2(data, 3)
            vers_2.append(accuracy)

        x = 0
        y = [0, 0]
        for i, v in enumerate(final_data):
            for num in v:
                x += num
            x = round(x / len(v), 2)
            y[i] = x
            x = 0

        deviation.append(abs(y[0] - y[1]))
        print(y[0], y[1])
        if y[0] > y[1]:
            old += 1
        elif y[1] > y[0]:
            new += 1

    for i in deviation:
        x += i
    x = round(x / len(deviation), 2)
    print('Deviation: {}'.format(x))
    print(old, new)

#average_data()
#average_data(1)
start2(new_data(), 1)
#start2(new_data(), 2)
#start2(new_data(), 3)
#start2(new_data(), 4)
#start2(new_data(), 5)
