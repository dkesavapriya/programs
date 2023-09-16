#pass or fail

mark=[]
n=int(input('Enter no. of subject:'))
for i in range(n):
    b=input()
    mark.append(b)
result=[]
for i in range(len(mark)):
    if int(mark[i])>=35:
        d=result.append('PASS')
    else:
        d=result.append('FAIL')
print(mark)
print(result)