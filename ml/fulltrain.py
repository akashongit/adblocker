#  fortraining 10 classifiers
from subprocess import call
import sys
print("\n")
for i in range(12):
    i = i+1
    print("*---------------------*")
    print("|Training "+str(i)+" th dataset|")
    print("*---------------------*")
    call(["python","%s.py"%argv[1],str(i)])
    print("\n\n")
