# splited the large dataset to 10 chunks
import pandas as pd
# from featuredict import features
bpath ='./dataset/unmodified/dmoz0409.csv'

df = pd.read_csv(bpath,nrows=1000000,encoding='latin1')
str_url = (df.iloc[:,:]).values.tolist()
print(str_url)
