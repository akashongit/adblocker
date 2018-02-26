import pandas as pd

bpath ='./dataset/dmoz0409_finaltest.csv'
df = pd.read_csv(bpath)
new_df = df.sample(frac=1)
new_df.to_csv(bpath,encoding='utf-8',index=False)
