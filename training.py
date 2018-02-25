from featuredict import features
import numpy as np
import pandas as pd
import nltk

csvfile = pd.read_csv("./datasets/dmoz0409_Arts_finaltest.csv")
# # str_url = (t.iloc[:,1:]
urls = csvfile.values.tolist()

fullset =[]

for content in urls:
    url_class = features.copy()
    url_class[content[0]]=True
    url_class[content[1]]=True
    url_class[content[2]]=True
    url_class[content[3]]=True
    fullset.append(url_class)

print(fullset)
