import pandas as pd
import nltk
import re
lis = []
a = []

df = pd.read_csv("./dataset/unmodified/dmoz0409_test.csv")
# bpath ='./features.txt'

features = set()
# features.add('_paddingbit1')
# features.add('_paddingbit2')
# features.add('_paddingbit3')
# features.add('_paddingbit4')
# for content in urls:
#     features.add(content[0])
#     features.add(content[1])
#     features.add(content[2])
#     features.add(content[3])
# print (t.ix[:,1:])
# str_url = (df.iloc[:,1:2])
# str_class = (df.iloc[:,2:])

str_url = (df.iloc[:,0:1])

urls = str_url.to_string(index = False)

list_urls = urls.split('\n')

for row in list_urls:
    nrow = re.sub("[\s!@#$+_.\-/:=&?~\d]",' ', row)
    # print(nrow)

    n = 4
    fourgrams = nltk.ngrams(nrow.split(), n)

    for grams in fourgrams:
        l = list(grams)
        # print(l)
        features.add(l[0])
        features.add(l[1])
        features.add(l[2])
        features.add(l[3])


# df = pd.read_csv("./datasets/dmoz0409_Arts_finaltest.csv")
# # str_url = (t.iloc[:,1:]
# urls = df.values.tolist()
# # myiter = iter(urls)
#
#

# print(features)
featureset = list(features)
# print(featureset)
# print("hotstar" in featureset)
print("No of words : ",len(featureset))
fd = open("./featuredict.py",'w', encoding="utf-8")
fd.write("features = { \"_paddingbit1\":False,\"_paddingbit2\":False,\"_paddingbit3\":False,\"_paddingbit4\":False,")
for line in featureset:
    # if("''" in list(line)):
        # print(line)
    con = '\"%s\" : False,'%line
    # print(con)
    fd.write(con)
fd.write("\n}")
fd.close()
