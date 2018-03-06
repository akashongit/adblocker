# predict
import pickle
import nltk
from featuredict import features
import sys
import re
from categories import ds
from collections import Counter

final_context = []

# def predict(url,category):
def predictcontext(url):

    featdict = {}

    featureset = re.sub('[\s!@#$+_.\-/:=&?~\d]',' ', url)

    templist = featureset.split(" ")
    templist = list(filter(None, templist)

    length = len(templist)
    if(length>3):
        n = 4
        grams = nltk.ngrams(featureset.split(), n)

    else:
        n = length

    grams = nltk.ngrams(featureset.split(), n)
    count = 0

    for gram in grams:
        count = count+1
        url_feature = features.copy()
        for val in range(3):
            try:
                if( gram[val] in url_feature ):
                    url_feature[gram[val]]=True
            except IndexError:
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
    print("The context for the url %s is %s"%(url,ds[context]))
    return ds[context]

if(sys.argv[1]):
    predictcontext(sys.argv[1])
