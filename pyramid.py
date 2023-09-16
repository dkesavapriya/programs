#pyramid

import string
alph=list(string.ascii_uppercase)
n= int(input('enter no:'))
for i in range(0,n):
    for j in range(0,i+1):
        print(alph[j],end=" ")
    if j>=1:
        for k in range(j-1,-1,-1):
            print(alph[k],end=" ")
    print('\n')