from subprocess import call
import pandas as pd
import sys
bpath ='./dataset/dmoz0409_finaltest.csv'
for i in range(10):
    print("Epoch %s"%i)
    df = pd.read_csv(bpath)
    new_df = df.sample(frac=1)
    new_df.to_csv(bpath,encoding='utf-8',index=False)
    call(["python","%s.py"%sys.argv[1],str(i)])
