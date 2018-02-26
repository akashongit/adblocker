from featuredict import features
# import numpy as np
import pandas as pd
import nltk
import pickle
from categories import ds
import sys
from random import randint

padbits = ["_paddingbit1","_paddingbit2","_paddingbit3","_paddingbit4"]
# category = ds[int(sys.argv[1])-1]
# bpath ='./dataset/dmoz0409_%s_finaltest.csv'%category
bpath ='./dataset/dmoz0409_finaltest.csv'
# print(bpath)
csvfile = pd.read_csv(bpath)
# # str_url = (t.iloc[:,1:]
urls = csvfile.values.tolist()

fullset =[]

for content in urls[:3000]:
    url_class = features.copy()
    try:
        url_class[content[0]]=True
        url_class[content[1]]=True
        url_class[content[2]]=True
        url_class[content[3]]=True
    except KeyError:
        val = randint(0, 3)
        url_class[padbits[val]] = True

    res = content[4]
    # if content[4] == -1:
        # res = "neg"
    # else :
        # res = "pos"
    fullset.append((url_class,res))
    # fullset.append(url_class)
    # print(fullset)
# print(url_class)
# training_set = urlclass[:1900]
#
# # set that we'll test against.
training_set = fullset
# print(fullset)
testing_set = fullset[100:]
# print(testing_set)
print("Training NaiveBayesClassifier...\n")
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Successfully trained!!!")

save_classifier = open("./classifiers/naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

msg = " Classifier accuracy percent: "+str(nltk.classify.accuracy(classifier, testing_set)*100)
print(msg)

save_classifier = open("./classifiers/naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

# fd = open("./accuracy.txt",'a',encoding = "utf-8")
# fd.write(category+msg+"\n")
# fd.close()
# testset [(,,,)]
# classifier_f = open("./classifiers/naivebayes%s.pickle"%category, "rb")
# classifier = pickle.load(classifier_f)
# classifier_f.close()
