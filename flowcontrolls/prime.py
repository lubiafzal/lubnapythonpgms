num=13
flag=0

for i in range(2,num):
    if(num%i==0):
        flag==1
        break
print(f"{num} is not prime")

if flag==0:
    print(f"{num} is prime")
