from random import *
print "Sisesta jarjendi pikkus: ",
n=input()
jarjend=[]
for j in range(n):
    jarjend.append(randint(1,99))
for i in range(n):
    for j in range(i+1):
        if i == j:
           continue 
        elif (jarjend[j] == jarjend[i]):
            print "Jarjendi " +str(i) +". liige on sama jarjendi " +str(j) +". liikmega"
        else:
            continue
print jarjend
