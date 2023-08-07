myobject=open("mames.txt",'r')
d=myobject.readlines()
for line in d:
    words=line.split()
    print(words)
