# aggregate the prediction of 10 classifiers and gives mode
import pickle
import nltk
from sgdcfeaturedict import features
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

    grams = nltk.ngrams(featureset.split(), n)
    # print(fourgrams)
    count = 0

    for gram in grams:
        count = count+1
        url_feature = features.copy()
        # print("\ncontext %s"%count)
        for val in range(3):
            if( gram[val] in url_feature ):
                url_feature[gram[val]]=True
            else:
                url_feature[val] = True

        testdata=[]
        testdata.append(list(url_feature.values())
        # testdat;;a = [(url_feature,None)]
        # print(testdata)
        classifier_f = open("./classifiers/sgdc.pickle", "rb")
            # print("svm%s classifier loaded"%val)
        classifier = pickle.load(classifier_f,encoding='latin1')
            # result = classifier.classify(testdata[0])
        result = classifier.predict(testdata)
        final_context.append(result)
            # print(result)
        print("Context : ",ds[int(result)])
        classifier_f.close()
        # return str(ds[result])
    data = Counter(final_context)
    print("Output")
    context = int(data.most_common(1)[0][0])
    # print(context)
    print("The context for the url %s is %s"%(url,ds[context]))
    return ds[context]
predictcontext(sys.argv[1])
# predictcontext(sys.argv[1],sys.argv[2])
