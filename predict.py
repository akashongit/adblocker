import pickle
import nltk
from featuredict import features
import sys
import re
from random import randint
import numpy as np
from categories import ds

# def predict(url,category):
def predict(url):
    # classifier_f = open("./classifiers/naivebayes%s.pickle"%category, "rb")
    # classifier_f = open("./classifiers/svm%s.pickle"%category, "rb")
    classifier_f = open("./classifiers/naivebayes.pickle", "rb")
    classifier = pickle.load(classifier_f,encoding='latin1')

    url = sys.argv[1]
    featdict = {}

    # print(url)
    featureset = re.sub('[\s!@#$+_.\-/:=&?~\d]',' ', url)
    fourgrams = nltk.ngrams(featureset.split(), 4)
    # print(fourgrams)
    for grams in fourgrams:
        url_feature = features.copy()
        try:
            url_feature[grams[0]]=True
            url_feature[grams[1]]=True
            url_feature[grams[2]]=True
            url_feature[grams[3]]=True
        except KeyError:
                val = randint(0, 3)
                url_feature[padbits[val]] = True
        # print(grams)
        testdata=[]
        testdata.append((url_feature))
        # testdata = [(url_feature,None)]
    # print(testdata)
    result = classifier.classify(testdata[0])
    # print(ds[result])
    print(result)
    classifier_f.close()
predict(sys.argv[1])
# predict(sys.argv[1],sys.argv[2])
