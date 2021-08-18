from nltk.corpus import names
from nltk.classify import apply_features
import random, nltk


# In Machine Learning, using too many features is called overfitting.
# To counteract this, use a larger training set or pick better features

# Version 1:
'''def gender_features(word):
    return {'last_letter': word[-1]}

training_set = apply_features(gender_features, labeled_names[500:]) # Doesn't use much memory
testing_set = apply_features(gender_features, labeled_names[:500])
classifier = nltk.NaiveBayesClassifier.train(training_set)
# print(classifier.classify(gender_features('Neo')))
print(nltk.classify.accuracy(classifier, testing_set))
print(classifier.show_most_informative_features(15))'''




# Version 2
def start(list_of_names, path = 0):
    def gender_features2(name):  # Much better than version 1
        features = {}
        features['first_letter'] = name[0].lower()
        features['last_letter'] = name[-1].lower()
        features['middle_letter'] = name[(len(name) // 2)].lower()
        return features

    featuresets = [(gender_features2(n), gender) for (n,gender) in list_of_names]
    train_set, test_set = featuresets[500:], featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    if path == 1:
        print(nltk.classify.accuracy(classifier, test_set))
        print(classifier.show_most_informative_features(15))
    return nltk.classify.accuracy(classifier, test_set) * 100




# Using Error Analysis
def start2(list_of_names, path = 0):
    def gender_features3(name):  # Much better than version 1
        features = {}
        features['middle_letter'] = name[(len(name) // 2)]
        features['last_suffix'] = (name[-2:])
        features['first_prefix'] = (name[0] + name[1]).lower()
        return features

    def error_analysis():   # Each error dev sees, adjusts the features to meet it
        errors = []
        for (name, tag) in devtest_names:
            guess = classifier.classify(gender_features3(name))
            if guess != tag:
                errors.append((tag, guess, name))

        return sorted(errors)

    def print_errors():
        errors = error_analysis()
        for right_gender, guessed_gender, name in errors:
            print('correct: {}, guess: {}, name: {}\n'.format(right_gender, guessed_gender, name))

    train_names = list_of_names[500:]  # Used for training the model
    devtest_names = list_of_names[500:1500] # Used to perform error analysis
    test_names = list_of_names[:500]    # Used as a final evalulation

    train_set = [(gender_features3(n), gender) for (n, gender) in train_names]
    devtest_set = [(gender_features3(n), gender) for (n, gender) in devtest_names]
    test2_set = [(gender_features3(n), gender) for (n, gender) in test_names]

    featuresets = [(gender_features3(n), gender) for (n,gender) in list_of_names]
    test_set = featuresets[:500]
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    if path != 2:
        if path == 1:
            #print('Before Error Analysis: {}'.format(nltk.classify.accuracy(classifier, test_set)))
            #print_errors()

            print('After Error Analysis: {}'.format(nltk.classify.accuracy(classifier, test_set)))
            print(classifier.show_most_informative_features(100))
        return nltk.classify.accuracy(classifier, test_set) * 100
    user_input = input('Enter a name:\n')
    gender = classifier.classify(gender_features3(user_input))
    user_gender = input('Enter the gender:\n')
    print('Real Gender - {}\nGuessed Gender - {}'.format(user_gender, gender))

def new_names():
    labeled_names = ([(name, 'male') for name in names.words('male.txt')] +
                     [(name, 'female') for name in names.words('female.txt')])
    random.shuffle(labeled_names)
    return labeled_names

def average_data():
    deviation = []
    old, new = 0, 0
    for iteration in range(15):
        data = [vers_1, vers_2] = [], []
        for i in range(25):
            names = new_names()
            accuracy = start(names)
            vers_1.append(accuracy)
            accuracy = start2(names)
            vers_2.append(accuracy)

        x = 0
        y = [0, 0]
        for i, v in enumerate(data):
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

def all_start():
    names = new_names()
    start(names, 1)
    start2(names, 1)

#all_start()
#average_data()
names = new_names()
start2(names, 2)
