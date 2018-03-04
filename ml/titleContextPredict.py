from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

example_sent = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)
# word_tokens = ' '.join(map(str, word_tokenList))
# print(word_tokens)
# featureset = re.sub('[\s!@#$+_.\-/:=&?~\d]',' ', word_tokens)
# words = featureset
# print(featureset)
# templist = featureset.split(" ")
filtered_sentence = [w for w in word_tokens if not w in stop_words]
# print(word_tokens)
print(filtered_sentence)
