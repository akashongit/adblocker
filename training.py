from featuredict import features
import numpy as np
import pandas as pd
import nltk

csvfile = pd.read_csv("./dataset/dmoz0409_Arts_finaltest.csv")
# # str_url = (t.iloc[:,1:]
urls = csvfile.values.tolist()

fullset =[]

for content in urls[:3000]:
    url_class = features.copy()
    url_class[content[0]]=True
    url_class[content[1]]=True
    url_class[content[2]]=True
    url_class[content[3]]=True
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
testing_set = fullset[1900:]
print("Entered NaiveBayesClassifier")
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("learnt!!!")
print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)

save_classifier = open("naivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
