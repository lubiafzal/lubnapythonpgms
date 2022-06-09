arr1=[2,3,5,7,9,1,10]
arr2=[4,5,6,3,2,1,10]

arr1.sort()
arr2.sort()
p1=0
p2=0
while(p1<=len(arr1)-1 and p2<=len(arr2)-1):
    if arr1[p1]==arr2[p2]:
        print(f"common element is {arr1[p1]}")
        p1+=1
        p2+=1

    elif arr1[p1]>arr2[p2]:
        p2+=1
    elif arr1[p1]<arr2[p2]:
        p1+=1
arr=[1,22,34,11,23,14,56,21,41]
arr.sort()
print(arr)
print(sum(arr))
print(dir(arr))
print(sorted(arr))
ar=sorted(arr,reverse=True)
print(ar)
print(max(arr))