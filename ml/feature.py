import pandas as pd
#
t = pd.read_csv("./datasets/dmoz0409_Arts_finaltest.csv")
# # str_url = (t.iloc[:,1:]
urls = t.values.tolist()
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

fd = open("feature.txt",'w',encoding = "utf-8")
for line in featureset:
    fd.write(line+'\n')

fd.close()
