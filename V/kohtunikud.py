print "Sisesta kohtunike arv:",
n=input()
a=[]
if n<3:
    print "Otsi kohtunikke juurde ja tule siis tagasi."
else:
    for i in range(n):
        print str(i+1) +". kohtuniku pandud hinne:",
        h=input()
        a.append(h)
    print "Voistleja hindeks kujunes: "+str((sum(a)-(min(a))-(max(a)))/(float(n)-2))
