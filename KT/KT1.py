# -*- coding: cp1257 -*-
p=[15, 16, 14, 19, 20, 8]
t=[10, 14, 16, 18]

#arvutab poiste keskmise
summa=0.0
i=0
while i<len(p):
    summa+=int(p[i])
    i+=1
pkeskmine=summa/len(p)
print "%.2f" % (pkeskmine)

#arvutab tüdrukute keskmise
summa=0.0
i=0
while i<len(t):
    summa+=int(t[i])
    i+=1
tkeskmine=summa/len(t)
print "%.2f" % (tkeskmine)

#arvutab, mitu poissi sai üle tüdrukute keskmise
i=0
korgem=0
while i<len(p):
    if p[i]>tkeskmine:
        korgem=korgem+1
    i+=1
print korgem

#prindib kujul 15-16-14-19-20-8
print "-".join(str(v) for v in p if v>0)
print "-".join(str(v) for v in t if v>0)
