def pair(l,t):
    L= []
    for i in l:
        if t-i in l:
            L.append((i,t-i))
            l.remove(t-i)
    return(L)

l = eval(input("Enter list of numbers\ne.g. format: [1,2,3,4]"))
t = int(input("Enter target number: "))
print(pair(l,t))