import pickle
import nltk
from featuredict import features
import sys
import re

def predict(category):
    classifier_f = open("./classifiers/naivebayes%s.pickle"%category, "rb")
    classifier = pickle.load(classifier_f)

    url = sys.argv[1]
    featdict = {}

    print(url)
    featureset = re.sub('[\s!@#$+_.\-/:=&?~\d]',' ', url)
    fourgrams = nltk.ngrams(featureset.split(), 4)
    print(fourgrams)
    for grams in fourgrams:
        url_feature = features.copy()
        # try:
        print(grams)



    # result = classifier.classify()
    classifier_f.close()

predict("Arts")
