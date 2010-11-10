print "Mitu inimest on j2rjekorras?",
n=input()
korvid=[]
loendur=0
korv=0
for i in range (n):
    print "Mitu asja on " +str(i+1) +". inimesel korvis?",
    m=input()
    korvid.append(m)
for i in range ((len(korvid))-1):
    loendur==0
    if korvid[i]>3:
        loendur+=1
    if loendur==0:
        print str(i+2) +". inimese ees pole yhtegi inimest, kellel oleks korvis rohkem kui 3 eset"
    elif loendur==1:
        print str(i+2) +". inimese ees on 1 inimene, kelle korvis on rohkem kui 3 eset"
    else:
        print str(i+2) +". inimese ees on " +str(loendur) +" inimest, kellel on korvis rohkem kui 3 eset"
