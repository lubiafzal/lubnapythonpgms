arr=[1,2,3,14,12,13,15]
element=14
for num in arr:
    if element==num:
        print("element found")
        break
    else:
        print("element not found")


numbers=[1,-2,-3,4,5,6,0,3,2,0,-5,0,-6,0,-3]
p_count=0
p_count_sum=0
n_count=0
n_count_sum=0
z_count=0
for num in numbers:
    if num>0:
        p_count+=1
        p_count_sum+=num
    elif num<0:
        n_count+=1
        n_count_sum+=num
    elif num==0:
        z_count+=1
print(f"+ve count{p_count},-ve count{n_count},zero count{z_count}")
print(f"sum of positive numbers{p_count_sum},sum of negative numbers{n_count_sum}")

lst=[12,23,45,667,86,456,356,6685,45,32]
element=667
flag=0
for num in lst:
    if element==num:
        flag=1
        break
print("element found" if flag==1 else "element not found")
lst=[12,23,45,667,86,456,356,6685,45,32]
element=667
flag=0
for i in range(0,len(lst)):
    if element==lst[i]:
        flag=1
        break
print("element found" if flag==1 else "element not found")














