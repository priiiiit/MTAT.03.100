file=open("Keelumargid.txt","r")
kiirus=[]
aeg=[]
teepikkus=[]
sisend=[]
rida=0
f=0
while rida!="":
    rida=file.readline()
    for r in rida.split():
        sisend.append(r)
for i in range (len(sisend)):
    if (i%2)!=0:
        f=sisend[i]
        kiirus.append(f)
    elif (i%2)==0:
        f=sisend[i]
        teepikkus.append(f)
aeg.append(float(teepikkus[0])/90)
for i in range (len(teepikkus)-1):
    aeg.append(((float(teepikkus[i+1]))-(float(teepikkus[i])))/(float(kiirus[i])))
print "Aeg kokku: " +str(sum(aeg))
