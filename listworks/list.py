
expenses=[12000,13000,12000,16000]
for amount in expenses:
    print(amount)

expenses=[123,345,567,654,321,123]
print(expenses[-1])

for i in range(0,6):
    print(expenses[i])
names=["java","c++","c","python"]
for i in range(0,4):
    print(names[i])
for lang in names:
    print(lang)

print(names[0])
print(len(names))

lst=[12,23,34,45,56,67]
lst.append(49)
print(lst)

names=["java","c++","c","python"]
for i in range(0,len(names)):
    print(names[i])

employee_names=["rahul","jabir","dev","krishna"]
for name in employee_names:
    print(name)
for i in range(0,len(employee_names)):
    print(employee_names[i])

numbers=[12,13,14,15,16,17,18,19,20]
for num in numbers:
    if num%2==0:
         print(num)

num=[11,12,13,14,15,16,17,18,19]
for n in num:
    if n==15:
        print(n)
    elif n>15:
        print(n+1)
    elif n<15:
        print(n-1)
#   print count of numbers from 14 to 18

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






























