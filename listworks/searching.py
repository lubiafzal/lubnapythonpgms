arr=[1,2,3,14,12,13,15]
element=14
for num in arr:
    print("element found" if num==element else "not found")


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