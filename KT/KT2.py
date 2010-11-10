# -*- coding: cp1257 -*-
#küsib poiste arvu
print "Sisesta poiste arv:"
arv=input()

#loob järjendi
from random import *
tulemus=[]

#loob suvalised tulemused
for i in range(arv):
    tulem=randint(0,20)
    tulemus.append(tulem)

print "Poiste tulemused olid: "
print "-".join(str(v) for v in tulemus if v>=0)

#leiab minimaalse
maksimaalne=20
for tulem in tulemus:
    if(tulem<maksimaalne):
        maksimaalne=tulem
mini=maksimaalne

#leiab maksimaalse
minimaalne=0
for tulem in tulemus:
    if (tulem>minimaalne):
        minimaalne=tulem
maks=minimaalne

print "Väikseim tulemus: "+str(tulemus.index(mini)+1)+". poisil("+str(mini)+"p)"
print "Suurim skoor "+str(tulemus.index(maks)+1)+". poisil ("+str(maks)+"p)"
