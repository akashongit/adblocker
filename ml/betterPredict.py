# aggregate the prediction of 10 classifiers and gives mode
import pickle
import nltk
from featuredict import features
import sys
import re
# from random import randint
# import numpy as np
from categories import ds
from collections import Counter

final_context = []

# def predict(url,category):
def predictcontext(url):
    # classifier_f = open("./classifiers/naivebayes%s.pickle"%category, "rb")
    # classifier_f = open("./classifiers/svm%s.pickle"%category, "rb")
    # classifier_f = open("./classifiers/naivebayes.pickle", "rb")
    # classifier_f = open("./classifiers/svm.pickle", "rb")
    # classifier = pickle.load(classifier_f,encoding='latin1')

    # url = sys.argv[1]
    featdict = {}

    # print(url)
    featureset = re.sub('[\s!@#$+_.\-/:=&?~\d]',' ', url)
    # print(featureset)
    templist = featureset.split(" ")
    templist = list(filter(None, templist))
    # print(templist)
    length = len(templist)
    if(length>3):
        n = 4
        grams = nltk.ngrams(featureset.split(), n)

    else:
        n = length
        # print("No of words %s"%n)

    grams = nltk.ngrams(featureset.split(), n)
    # print(fourgrams)
    count = 0

    for gram in grams:
        count = count+1
        url_feature = features.copy()
        # print("\ncontext %s"%count)
        for val in range(3):
            if( gram[val] in url_feature ):
                try:
                    url_feature[gram[val]]=True
                except Exception as e:
                    url_feature[val] = True

            else:
                url_feature[val] = True
        testdata=[]
        testdata.append((url_feature))

        classifier_f = open("./classifiers/svm10.pickle", "rb")
        classifier = pickle.load(classifier_f,encoding='latin1')
        result = classifier.classify(testdata[0])
        final_context.append(result)
        print("Context : ",ds[int(result)])
        classifier_f.close()
    data = Counter(final_context)
    print("Output")
    context = int(data.most_common(1)[0][0])
    # print(context)
    print("The context for the url %s is %s"%(url,ds[context]))
    return ds[context]
# predictcontext(sys.argv[1])
