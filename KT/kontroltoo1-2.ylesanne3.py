skoor=open("poisid_2.txt","r")
nimed=open("nimed_2.txt","r")
rida=skoor.readline()
rida2=nimed.readline()
skoor=[]
nimed=[]
for i in rida.split():
    skoor.append(int(i))
sum=0.0
for i in range (len(skoor)):
    sum+=skoor[i]
avg=(sum)/(len(skoor))
poissn=0
for i in range (len(skoor)):
    if abs((skoor[i])-avg)<poissn:
        poissn=i
for i in rida2.split():
    nimed.append(i)
print "Poiste nimed: " +" ".join(str(v) for v in nimed if v>0) 
print "Poiste skoorid:" +"-".join(str(v) for v in skoor if v>0)
print "Keskmiseks tulemuseks on: " +str((round(avg, 2)))
print "Koige lahemal keskmisele tulemusele oli " +str(nimed[poissn])
