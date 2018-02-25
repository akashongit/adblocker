import pandas as pd
from categories import ds
import sys
category = ds[int(sys.argv[1])-1]
bpath ='./dataset/dmoz0409_%s_finaltest.csv'%category
csvfile = pd.read_csv(bpath)
# # str_url = (t.iloc[:,1:]
urls = csvfile.values.tolist()
# # myiter = iter(urls)
#
#
features = set()
for content in urls:
    features.add(content[0])
    features.add(content[1])
    features.add(content[2])
    features.add(content[3])
# print(features)
featureset = list(features)

featuredict = {}
for feature in featureset:
    featuredict[feature] = False

print("featureset sucessfully prepared!!!\n")

# print(featuredict)



# print(featureset)



# import nltk
# # nltk.download('movie_reviews')
# import random
# from nltk.corpus import movie_reviews
#
# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]
#
# random.shuffle(documents)
#
# all_words = []
#
# for w in movie_reviews.words():
#     all_words.append(w.lower())
#
# all_words = nltk.FreqDist(all_words)
#
# word_features = list(all_words.keys())[:3000]
#
# print(word_features)
#
# def find_features(document):
#     words = set(document)
#     features = {}
#     for w in word_features:
#         features[w] = (w in words)
#
#     return features

# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))
# featuresets = [(find_features(rev), category) for (rev, category) in documents]
# print(featuresets)
