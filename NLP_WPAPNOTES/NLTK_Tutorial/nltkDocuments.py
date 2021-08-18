from nltk.corpus import movie_reviews
import random, nltk, pickle
from nltk.classify.scikitlearn import SklearnClassifier

from sklearn.naive_bayes import MultinomialNB, BernoulliNB  # The classifiers
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)
all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000]   # Gets as much frequent words as possible

def find_features(document):
    word = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in word)
    return features

featuresets = [(find_features(rev), category) for (rev, category) in documents]
training_set, testing_set = featuresets[:1900], featuresets[1900:]

#classifier = nltk.NaiveBayesClassifier.train(training_set)

'''with open('naivebayes.pickle', 'rb') as f:  # And now we can do this instead
    classifier = pickle.load(f) # Will make this much faster, so we don't need classifier above

print('O Naive Bayes Accuracy % - {}'.format(nltk.classify.accuracy(classifier, testing_set) * 100))
classifier.show_most_informative_features(15)




MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print('MNB_classifier Accuracy % - {}'.format(nltk.classify.accuracy(MNB_classifier, testing_set) * 100))



BNB_classifier = SklearnClassifier(BernoulliNB())
BNB_classifier.train(training_set)
print('BNB_classifier Accuracy % - {}'.format(nltk.classify.accuracy(BNB_classifier, testing_set) * 100))



LR_classifier = SklearnClassifier(LogisticRegression())
LR_classifier.train(training_set)
print('LR_classifier Accuracy % - {}'.format(nltk.classify.accuracy(LR_classifier, testing_set) * 100))



SGD_classifier = SklearnClassifier(SGDClassifier())
SGD_classifier.train(training_set)
print('SGD_classifier Accuracy % - {}'.format(nltk.classify.accuracy(SGD_classifier, testing_set) * 100))



SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print('SVC_classifier Accuracy % - {}'.format(nltk.classify.accuracy(SVC_classifier, testing_set) * 100))



LSVC_classifier = SklearnClassifier(LinearSVC())
LSVC_classifier.train(training_set)
print('LSVC_classifier Accuracy % - {}'.format(nltk.classify.accuracy(LSVC_classifier, testing_set) * 100))



NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print('NuSVC_classifier Accuracy % - {}'.format(nltk.classify.accuracy(NuSVC_classifier, testing_set) * 100))'''






'''with open('naivebayes.pickle','wb') as f:   # Will make this run faster
    pickle.dump(classifier, f)'''
