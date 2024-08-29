from math import sqrt
l=[]

for i in range(5):
    n = int(input("Enter number: "))
    l.append(n)

l.sort()
print(l)
t = l[0]

t1=[]
for i in range(1,n//2+1):
    if t%i==0:
        t1.append(i)

t1 = t1[::-1]
print(t1)

for i in t1:
    if l[0]%i==l[1]%i==l[2]%i==l[3]%i==l[4]%i==0:
        print("Greatest divisor =", i)
        break