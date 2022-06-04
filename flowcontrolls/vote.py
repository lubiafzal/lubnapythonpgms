# age=18
#
# if (age>=18):
#     print("eligible for voting")
#
# else:
#     print("not eligible")
#


#
# num=15
# if (num>0):
#     print(f"{num} is +ve")
# else:
#     print(f"{num}is -ve")

# num1=10
# num2=20
# if (num1>num2):
#     print(f"the largest number is {num1}")
# else:
#     print(f"the largest number is {num2}")

# num=12
# if (num%2==0):
#     print("even")
# else:
#     print("odd")
# num=12
# print("even" if num%2==0 else "odd")
#
# num=15
# print("+ve" if num > 0 else "-ve")
#
# num1=10
# num2=20
# print(num1 if num1>num2 else  num2)

num=15

if  (num/3==1):
    print("fizz")
elif (num/5==1):
    print("buzz")
if (num/15==1):
    print("fizzbuzz")

else:
    print("cant find")


def check_num(num):
    return "even" if num%2==0 else "odd"


print(check_num(46))


cname="luminar"
print(cname.startswith("l"))

def startend(name):
    return name.startswith("s")
print(startend("sjjhgffee"))


def validate_email(email):
    return email.endswith("@gmail.com")
print(validate_email("adfgc"))


def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
print(factorial(5))

for row in range(1,5):
    for col in range(1,5):
        print(col,end=" ")
    print()


def is_prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break
    return True if flag==0 else False
print(is_prime(9))

def prime_range(low,up):
    for num in range(low,up):
        if is_prime(num):
            print(num)
prime_range(3,15)











