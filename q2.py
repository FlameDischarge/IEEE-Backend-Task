'''
i have no idea how i did this code
'''
from math import ceil

n = int(input("Enter n: "))

list = [[0 for i in range(n)] for i in range(n)]

u = n-1
l = 0

r=c=0
no = 1

for x in range(ceil(n/2)):

    while c<u:
        list[r][c] = no; no+=1
        if c<u:
            c+=1
    if no==n**2+1:
            break
    

    while r<u:
        list[r][c] = no; no+=1
        if r<u:
            r+=1
    if no==n**2+1:
            break

    while c>l:
        list[r][c] = no; no+=1
        if c>l:
            c-=1
    if no==n**2+1:
            break
    

    while r>l:
        list[r][c] = no; no+=1
        if r>l:
            r-=1
    if no==n**2+1:
            break
    
    c+=1
    r+=1
    u-=1
    l+=1

if n%2!=0:
    r=c=(n+1)//2-1
    list[r][c] = n**2

for i in list:
     for j in i:
          print(j,end=' '*(2+len(str(n**2))-len(str(j))))
     print()