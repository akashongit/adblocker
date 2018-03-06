# predict title context
import pickle
import nltk
from titleDict import features
import sys
import re
from categories import ds
from collections import Counter


final_context = []

def predictTitleContext(title):
    featdict = {}
    featureset = re.sub('[\s!@#$+_.\-/:=&?~\d]',' ', title)
    templist = featureset.split(" ")
    templist = list(filter(None, templist))
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
        title_feature = features.copy()
        for val in range(3):
            try:
                if( gram[val] in title_feature ):
                    title_feature[gram[val]]=True
            except IndexError:
                title_feature[val] = True

            else:
                title_feature[val] = True
        testdata=[]
        testdata.append((title_feature))

        classifier_f = open("./classifiers/titleSvm.pickle", "rb")
        classifier = pickle.load(classifier_f,encoding='latin1')
        result = classifier.classify(testdata[0])
        final_context.append(result)
        print("Context : ",ds[int(result)])
        classifier_f.close()
    data = Counter(final_context)
    print("Output")
    context = int(data.most_common(1)[0][0])
    print("The context for the title %s is %s"%(title,ds[context]))
    return ds[context]

# if(sys.argv[1]):
    # predictTitleContext(sys.argv[1])
