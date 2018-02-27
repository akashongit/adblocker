import pandas as pd
from categories import ds
import re
ran = 15
length = 14999
bpath ='./dataset/unmodified/dmoz0409_ds_test.csv'
fd = open(bpath, 'w',encoding = "utf-8")

for i in range(ran):
    category = ds[i]
    df = pd.read_csv("./datasets/dmoz0409_%s_test.csv"%category)
    str_url = (df.iloc[:,1:2]).values.tolist()
    str_class = (df.iloc[:,2:]).values.tolist()
    # length = len(str_class)
    # print(str_class)
    for index in range(length):
        # print(str(str_url[ind]))
        clas = str_class[index][0]
        # print(clas)
        if clas== 1:
            line = str_url[index][0]+','+str(i)+"\n"
            # print(line)
            fd.write(line)

fd.close()

##shuffle
bpath ='./dataset/unmodified/dmoz0409_ds_test.csv'
df = pd.read_csv(bpath)
new_df = df.sample(frac=1)
new_df.to_csv('./dataset/unmodified/dmoz0409_test.csv',encoding='utf-8',index=False)
# fd = open('./dataset/unmodified/dmoz0409_test.csv', 'w',encoding = "utf-8")
# str_url = (new_df.iloc[:,0:1]).values.tolist()
# str_class = (new_df.iloc[:,1:]).values.tolist()
# # print(str_url)
# length = len(str_class)
# index = 0
# for index in range(length):
#     # print(str(str_url[ind]))
# #     # clas = str_class[index][0]
# #     # print(clas)
#     line = str_url[index][0]+','+str()+"\n"
# #     # print(line)
#     fd.write(line)
# fd.close()
