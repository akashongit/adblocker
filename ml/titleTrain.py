#  train svm with 500 title dataset
from featuredict import features
import pandas as pd
import nltk
import pickle
from categories import ds
from random import randint
from sklearn.svm import LinearSVC
import sys

# try:
    # number = sys.argv[1]
# except Exception as e:
    # number = 10

classif = nltk.classify.scikitlearn.SklearnClassifier(LinearSVC())

padbits = ["_paddingbit1","_paddingbit2","_paddingbit3","_paddingbit4"]

src ='./dataset/titleTest.csv'

csvfile = pd.read_csv(src)

urls = csvfile.values.tolist()

fullset =[]
updateFullset = []
for content in urls[:20000]:
    url_class = features.copy()
    try:
        url_class[content[0]]=True
        url_class[content[1]]=True
        url_class[content[2]]=True
        url_class[content[3]]=True
    except KeyError:

        url_class[padbits[val]] = True

    res = content[4]

    fullset.append((url_class,res))

training_set = fullset
print("Training SVM")
# classifier = classif.train(training_set)

training_set[:]=[]

print("Successfully trained!!!")
print(" saved to ./classifiers/titleSvm.pickle")
# save_classifier = open("./classifiers/titleSvm.pickle","wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()

# msg = " Classifier accuracy percent: "+str(nltk.classify.accuracy(classifier, testing_set)*100)
# print(msg)
