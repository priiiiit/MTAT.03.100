# -*- coding: cp1257 -*-
#loeb faili ja jaotab �ra
p=open("poisid_2.txt", "r")
po=p.readline()
pois=po.split()
print "poiste tulemused:"
print "-".join(str(v) for v in pois if v>=0)

#leiab poiste keskmise
summa=0.0
i=0
while i<len(pois):
    summa+=int(pois[i])
    i+=1
pkeskmine=summa/len(pois)
print str("%.2f" % (pkeskmine))+" on keskmine poiste tulemus"

#teeb listi tulemuse ja keskmise vahega
i=0
uus=[]
while i<len(pois):
    uus.append(abs(float(pois[i])-float(pkeskmine)))
    i+=1

#leiab minimaalse
maksimaalne=20
for tulem in uus:
    if(tulem<maksimaalne):
        maksimaalne=tulem
mini=maksimaalne
minix=uus.index(mini)

#avab nimedefaili ja jaotab selle ning v�tab l�hima keskmise indeksiga nime
n=open("nimed_2.txt", "r")
ni=n.readline()
nim=ni.split()
print "Perekonnanimega: "+str(nim[minix])+" tulemus oli k�ige l�hemal poiste keskmisele tulemusele."
