import pandas as pd
from categories import ds
import re
ran = 15
length = 14999
bpath ='./dataset/dmoz0409_ds_finaltest.csv'
fd = open(bpath, 'w',encoding = "utf-8")

for i in range(ran):
    category = ds[i]
    df = pd.read_csv("./datasets/dmoz0409_%s_test.csv"%category)
    str_url = (df.iloc[:,1:2]).values.tolist()
    str_class = (df.iloc[:,2:]).values.tolist()
    # length = len(str_class)
    # print(str_class)
    for ind in range(length):
        # print(str(str_url[ind]))
        clas = str_class[ind][0]
        # print(clas)
        if clas== 1:
            line = str(str_url[ind])+','+str(i)+"\n"
            # print(line)
            fd.write(line)

fd.close()

##shuffle
bpath ='./dataset/dmoz0409_ds_finaltest.csv'
df = pd.read_csv(bpath)
new_df = df.sample(frac=1)
new_df.to_csv('./dataset/dmoz0409_finaltest.csv',encoding='utf-8',index=False)
# fd = open(bpath, 'w',encoding = "utf-8")
