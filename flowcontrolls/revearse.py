num=100
while(num!=0):
    last_digit=num%10
    print(last_digit)
    num=num//10

num=123
res=" "
while(num!=0):
    last_digit=num%10
    res+=str(last_digit)
    num=num//10
print(res)

num=123
res=0
while(num!=0):
    last_digit=num%10
    res=(res*10)+last_digit
    num=num//10
print(res)

num=123
res=""
while(num!=0):
    last_digit=num%10
    res+=str(last_digit)
    num=num//10
print(res)