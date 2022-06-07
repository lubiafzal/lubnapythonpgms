lst=[34,54,67,53,64,32,677,87,53,99,86,54,32]
evenlst=[]
for num in lst:
    if num%2==0:
        evenlst.append(num)
print(evenlst)
evenlst.sort()
print(evenlst)
evenlst.sort(reverse=True)
print(evenlst)
evenlst.insert(3,100)
print(evenlst)
print(lst.count(53))
evenlst.remove(54)
print(evenlst)
evenlst.pop()
print(evenlst)

