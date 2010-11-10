file=open("arvud.txt","r")
arv=0
arvud=[]
rida=0
while rida!="":
    rida=file.readline()
    for r in rida.split():
        arvud.append(r)
print arvud
for i in range (len(arvud)):
    if str(i+1) in arvud:
        continue
    else:
        print" Koik arvud pole esindatud"
    break
