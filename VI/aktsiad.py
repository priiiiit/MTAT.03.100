file=open("Aktsiad.txt","r")
rida=file.readline()
hinnad=rida.split()
file.close()
print "Mitut eelnevat paeva soovid keskmise arvutamisel kasutada? ",
k=int(raw_input())
for j in range(k,len(hinnad)+1):
    keskm=0
    for i in range(1,k+1):
        keskm=keskm+float(hinnad[j-i])
    keskm=float(keskm)/k
    print "%i-ndale paevale eelnenud %i paeva keskmine oli %f" % (j,k,keskm)
