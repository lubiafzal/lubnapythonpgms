arr=[2,3,5,4,1,8,9]
element=16
arr.sort()
flag=0
low=0
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
print("element found " if flag==1 else "not found")
