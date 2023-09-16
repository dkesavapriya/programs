'''Input: n = 4, time = 5
Output: 2

Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
After five seconds, the pillow is given to the 2nd person'''


n=int(input('Enter number of player:'))
t=int(input('Enter number of second:'))
a=[]
for i in range(1,n+1):
     b=a.append(i)
     if i==n:
         for i in range(1,n):
               b=a.append(n-i)
print(a[t%len(a)])