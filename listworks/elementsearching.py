arr=[2,4,3,6,7,33,22,11,77,99,56]
arr.sort()
print(arr)
flag=0
low=0
count=1
element=99
upp=len(arr)-1
while(low<=upp):
    mid=(low+upp)//2
    if element==arr[mid]:
        flag=1
        break
    elif element>arr[mid]:
        low=mid+1
    elif element<arr[mid]:
        upp=mid-1
    count+=1
print("element found" if flag==1 else "not found")
print(count)

