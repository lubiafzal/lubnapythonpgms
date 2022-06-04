#1**3+2**3+3**3=36
# num=3
#
# for i in range(1,4):
#
#     print(f"{i}**{num}=={i**num}")

num=153
sum=0
while(num!=0):
    last_digit=num%10
    cube=last_digit**3
    print(cube)
    sum=sum+cube
    num=num//10
print(sum)

