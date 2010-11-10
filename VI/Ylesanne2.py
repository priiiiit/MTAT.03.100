##################
## Paneb suvalised jarjendis olevad arvud suuruse jarjekorda
##################
jarjend=[5,2,1,4,3]
n=len(jarjend)
for i in range(n):
    for j in range(n):
        if (jarjend[j]>jarjend[i]):
            jarjend[i], jarjend[j]=jarjend[j],jarjend[i]
print jarjend
