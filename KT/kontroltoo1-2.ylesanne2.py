from random import *
print "Sisesta poiste arv: ",
nxx=input()
poisid=[]
vahe=0
poiss1=0
poiss2=0
for i in range (nxx):
    poisid.append(randint(1,20))
print "-".join(str(v) for v in poisid if v>0)
xxmin=20
xxmax=0
nmax=0
nmin=0
for i in range (nxx):
    if poisid[i]>=xxmax:
        xxmax=poisid[i]
        nmax=(i+1)
    elif poisid[i]<=xxmin:
        xxmin=poisid[i]
        nmin=(i+1)
    else:
        continue
print "Suurim skoor oli " +str(nmax) +". poisil (" +str(xxmax) +"p)"
print "Vaikseim skoor oli " +str(nmin) +". poisil (" +str(xxmin) +"p)"
