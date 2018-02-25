import pandas as pd
import nltk
import re
# from collections import Counter
# lis =()
lis = []
bpath ='./datasets/dmoz0409_Arts_finaltest.csv'
t = pd.read_csv("./datasets/dmoz0409_Arts_test.csv")
# print (t.ix[:,1:])
str_url = (t.iloc[:,1:2])
str_class = (t.iloc[:,2:])

urls = str_url.to_string(index = False)
# clas = str_class.to_string(index = False)
clas = str_class.values.tolist()
cleaned_urls = []
# print(clas)
myiter = iter(clas)
list_urls = urls.split('\n')
fd = open(bpath, 'w',encoding = "utf-8")
fd.write("text1,text2,text3,text4,istrue\n")
for row in list_urls:
    try:
        url_clas = next(myiter)
    except Exception as e:
        pass
    # print(type(row))
    nrow = re.sub('[\s!@#$+_.\-/:=&?~\d]',' ', row)
    # printpass)
    # tokens = nltk.word_tokenize(nrow)
    # print(tokens)
    # fourgrams=nltk.collocations.QuadgramCollocationFinder.from_words(tokens)
    # for fourgram, freq in fourgrams.ngram_fd.items():
        # print (fourgram)
    n = 4
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
      print(url_str,end='')
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
