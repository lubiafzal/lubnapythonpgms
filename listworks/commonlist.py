lst1=[11,12,13,14,15,16,17,18]
lst2=[11,34,56,78,90,13,14,54]
lst3=[]
for i in range(0,len(lst1)):
    for j in range(0,len(lst2)):
        if lst1[i]==lst2[j]:
            lst3.append(lst2[j])
print(lst3)

lst1=[11,12,13,14,15,16,11,11,12,13,17,18]
lst2=[11,34,56,78,90,13,11,11,12,13,14,14,54]
lst3=[]
for num in lst1:
    if num in lst2:
        lst3.append(num)
print(lst3)