poisid=[15, 16, 14, 19, 20, 8]
tydrukud=[10, 14, 16, 18]
print "Poiste tulemused:"
print "-".join(str(v) for v in poisid if v>0)
print "Tydrukute tulemused:"
print "-".join(str(v) for v in tydrukud if v>0)
print "Poiste keskmine tulemus: ",
xy=0.0
for i in range (len(poisid)):
    xy+=poisid[i]
print round(xy/(len(poisid)), 2)
print "Tydrukute keskmine tulemus: ",
xx=0.0
for i in range (len(tydrukud)):
    xx+=tydrukud[i]
print round(xx/(len(tydrukud)), 2)
xxwin=0
for i in range(len(poisid)):
    if poisid[i]>(xx/(len(tydrukud))):
        xxwin+=1
print "Poiste arv, kelle tulemus on suurem tydrukute keskmisest: " +str(xxwin)




