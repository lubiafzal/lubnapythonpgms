

numbers=[11,12,13,14,15,16,17,18,19]
count=0
for i in range(3,8):
    count+=1
print(count)
numbers=[11,12,13,14,15,16,17,18,19]
count=0
for num in numbers:
    if num>13 and num<19:
        count+=1
print(count)
numbers=[11,12,13,14,15,16,17,18,19]
count=0
for num in numbers:
    if num in range(14,19):
        count+=1
print(count)

numbers=[1,-2,-3,4,5,6,0,3,2,0,-5,0,-6,0,-3]
p_count=0
n_count=0
z_count=0
for num in numbers:
    if num>0:
        p_count+=1
    elif num<0:
        n_count+=1
    elif num==0:
        z_count+=1
print(f"the count of positive numbers{p_count}")
print(f"the count of negative numbers{n_count}")
print(f"the count of zeros{z_count}")

numbers=[1,-2,-3,4,5,6,0,3,2,0,-5,0,-6,0,-3]
sum=0
for num in numbers:
    sum+=num
print(sum)