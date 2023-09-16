#reverse the words in a string

a=input('Enter the string:')
b=list(a)
c=''
d=''
for i in range(len(b)):
    if b[i]==' ' or i==len(b)-1 :
        c+=d[::-1]
        c+=b[i]
        d=''
    else:
        d+=b[i]
print(c)
