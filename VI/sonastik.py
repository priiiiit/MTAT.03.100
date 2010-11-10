sonastik=open("Sonastik.txt","r")
line=sonastik.read()
mix=[]
est=[]
eng=[]
rida=0
valik=""
term=""
while rida!="":
    rida=sonastik.readline()
    for r in rida.split("\t"):
        mix.append(r)
for i in range (len(mix)):
    if (i%2)!=0:
        f=mix[i]
        eng.append(f)
    elif (i%2)==0:
        f=mix[i]
        est.append(f)
#while valik!=0:
#    print "1) Eesti-Inglise"
#    print "2) Inglise-Eesti"
#    print "0) Lahku programmist"
#    valik=input()
#    if valik==1:
#        print "Otsitav Eesti keelne sona: "
#        term=raw_input()
#        if term in est:
#            print "Otsitav on olemas", term

print len(est)
print len(eng)
print len(mix)

print est(1)



