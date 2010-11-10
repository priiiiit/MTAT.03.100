file = open("Hinded.txt","r")
sum = 0.0
hindeid = 0
while True :
    rida = file.readline()
    if rida == "" : 
        break
    else:
        sum= sum + int(rida)
hindeid = hindeid + 1
file.close()
print "Kokku loeti failist " + str(hindeid) + " hinnet"
print "Hinnete keskmine on: " + str(float(sum)/hindeid)
