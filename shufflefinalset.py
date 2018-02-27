from subprocess import call
import pandas as pd
for i in range(10):
    bpath ='./dataset/dmoz0409_finaltest.csv'
    df = pd.read_csv(bpath)
    new_df = df.sample(frac=1)
    new_df.to_csv(bpath,encoding='utf-8',index=False)
    call(["python","%s.py"%argv[1],str(i)])
