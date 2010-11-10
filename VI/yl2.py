jarjend=[5,2,1,4,3]
n=len(jarjend)
for i in range(n): 
    for j in range(i+1):
        if (jarjend[j]>jarjend[i]):
            jarjend[i],jarjend[j]=jarjend[j],jarjend[i]
            print jarjend[j]
            print " "
            print jarjend[i]
