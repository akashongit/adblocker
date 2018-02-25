from subprocess import call
print("\n")
for i in range(12):
    i = i+1
    print("*---------------------*")
    print("|Training "+str(i)+" th dataset|")
    print("*---------------------*")
    call(["python","prepareds.py",str(i)])
    print("\n\n")
