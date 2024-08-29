#ok i am not entirely sure how the outputs need to be generated
#i will try to explain via comments

n = int(input("Enter number of customers: "))
l = []

for i in range(n):
    l1 = eval(input("Enter an inner array: \ne.g. format [1,2,3]\n"))
    l.append(l1)


d = {}

for i in l:
    for x in i:
        if x not in d:
            d[x]=1
        else:
            d[x]+=1

#finding top 3 most popular items
p = []
for k,v in d.items():
    p.append((v,k))
p.sort();p = p[::-1]

top_3 = []
for i in range(3):
    top_3.insert(0,p[i][1])

print(top_3)

r=[]

#ok so how this will work is i will list down all the customers who have viewed
#at least 1 item in common with the customer to whom the recommendation has to be given.
#then the top 3 popular products from that is taken

for customer in l:
    L = []
    d = {}
    l1 = []
    for item in customer:
        for customer1 in l:
            if item in customer1 and customer1 is not customer and customer1 not in l1:
                L.extend(customer1)
                l1.append(customer1)
    for i in L:
        if i not in d:
            d[i] = L.count(i)
    l1=[]
    for k,v in d.items():
        l1.append((v,k))
    l1.sort();l1=l1[::-1]
    if len(l1)<3:
        l1.extend(top_3)
    print(l1)
    op = []
    for i in l1:
        try:
            op.append(i[1])
        except TypeError:
            op.append(i)

    r.append(op[:3])

for i in r:
    print(i)