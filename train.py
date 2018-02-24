from pandas import read_csv
import nltk
import re
# from collections import Counter

t = read_csv("./datasets/dmoz0409_Arts_test.csv")
# print (t.ix[:,1:])
str_url = (t.ix[:,1:2])
str_class = (t.ix[:,2:])

urls = str_url.to_string(index = False)
clas = str_class.to_string(index = False)
cleaned_urls = []
# urls.lstrip()
list_urls = urls.split('\n')
for row in list_urls:
    # print(type(row))
    nrow = re.sub('[\s!@#$+_./:=]&?',' ', row)
    # print(nrow)
    # tokens = nltk.word_tokenize(nrow)
    # print(tokens)
    # fourgrams=nltk.collocations.QuadgramCollocationFinder.from_words(tokens)
    # for fourgram, freq in fourgrams.ngram_fd.items():
        # print (fourgram)
    n = 4
    fourgrams = nltk.ngrams(nrow.split(), n)
    for grams in fourgrams:
      print (grams)
    # cleaned_urls.append(nrow)
    # row = str(row)
    # print(nrow)
    # l = row.split('.').split('-').split('/').split('_').split('+')
    # string = "".join(l)
    # print (string)

# print(cleaned_urls)


# sentence = 'this is a foo bar sentences and i want to ngramize it'
# n = 4
# fourgrams = ngrams(nrow.split(), n)
# for grams in fourgrams:
#   print (grams)
