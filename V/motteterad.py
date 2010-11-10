from random import *
fortune=open("fortune.txt","r")
fortunes=[]
tera=fortune.read()
for i in tera.split("---"):
    fortunes.append(i)
print fortunes[(randint(1,len(fortunes)))]
