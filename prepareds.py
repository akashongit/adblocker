import pandas as pd
import nltk
import re
from categories import ds
# import sys
from subprocess import call
# from collections import Counter
# lis =()
lis = []
# arg = int(sys.argv[1])
# category = ds[arg-1]
# bpath ='./dataset/dmoz0409_%s_finaltest.csv'%category
# df = pd.read_csv("./dataset/unmodified/dmoz0409_%s_test.csv"%category)
bpath ='./dataset/dmoz0409_finaltest.csv'
df = pd.read_csv("./dataset/unmodified/dmoz0409_test.csv")
# print (t.ix[:,1:])
str_url = (df.iloc[:,1:2])
str_class = (df.iloc[:,2:])

# str_url = (df.iloc[:,0:1])
# str_class = (df.iloc[:,1:])

urls = str_url.to_string(index = False)
# clas = str_class.to_string(index = False)
# print(urls)
clas = str_class.values.tolist()
cleaned_urls = []
# print(clas)
myiter = iter(clas)
list_urls = urls.split('\n')
fd = open(bpath, 'w',encoding = "utf-8")
fd.write("text1,text2,text3,text4,class\n")
for row in list_urls:
    try:
        url_clas = next(myiter)
        # print(row)
    except Exception as e:
        pass
    # print(type(row))
    nrow = re.sub("[\s!@#$+_.\-/:=&?~\d]",' ', row)
    # new_row = re.sub("[\]\[\']",'', nrow)
    # printpass)
    # tokens = nltk.word_tokenize(nrow)
    # print(tokens)
    # fourgrams=nltk.collocations.QuadgramCollocationFinder.from_words(tokens)
    # for fourgram, freq in fourgrams.ngram_fd.items():
        # print (fourgram)
    n = 4
    # fourgrams = nltk.ngrams(new_row.split(), n)
    fourgrams = nltk.ngrams(nrow.split(), n)
    # forgrams = filter(None,list(fourgrams))
    # forgrams = [list(x) for x in fourgrams]
    # forgrams = list(fourgrams)
    # if forgrams != []:
    # if fourgrams != []:
        # print(forgrams)
        # lis.append(next(myiter))
        # lis.append(forgrams)
        # lis = lis + tuple(next(myiter))
        # lis = lis + tuple(fourgrams)
    for grams in fourgrams:
      # nlist = list(grams)
      url_str =','.join(grams)+','+str(url_clas[0])+'\n'
      # print(url_str,end='')
      line = url_str
      fd.write(line)
    # cleaned_urls.append(nrow)
    # row = str(row)
    # print(nrow)
    # l = row.split('.').split('-').split('/').split('_').split('+')
    # string = "".join(l)
    # print (string)
# print(cleaned_urls)
# print(lis)

# sentence = 'this is a foo bar sentences and i want to ngramize it'
# n = 4
# fourgrams = ngrams(nrow.split(), n)
# for grams in fourgrams:
#   print (grams)
# print (str(fourgrams))
fd.close()
print("\ndataset sucessfully prepared!!!\n")
# call(["python","featureset.py",str(arg)])
# call(["python", "training.py",str(arg)])
