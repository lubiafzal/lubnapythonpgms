# def substract(n1,n2):
#     return n1-n2
# print(substract(5,10))
#
# def cube(num):
#     return num**3
#
# print(cube(3))
#
# def add(n1,n2):
#     add=n1+n2
#     return add
# print(add(23,45))
#
# def min(n1,n2):
#  return n1 if n1<n2 else n2
# print(min(2,45))
# def smart_sum(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1
# print(smart_sum(2,34))

# def check(n1):
#     return "even" if n1%2==0 else "odd"
# print(check(87))





# def validate_gmail(email):
#     return email.endswith("@gmail.com")
# print(validate_gmail("avc.@gmail.com"))
#
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     return fact
# print(factorial(5))





























# numbers=range(1,111)
# ans=sum(numbers)
# print(ans)
#
#
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)

# total=sum(range(1,101))
# print(total)
#
# low=min(range(43,56))
# print(low)

# def cube(num):
#
#     return num**3
# print(cube(3))
#
# def sub(n1,n2):
#
#     return n1-n2
# print(sub(12,3))
#
#
# def sum(n1,n2):
#     return n1+n2
# print(sum(12,34))
#
#
#
# def super_sub(n1,n2):
#     return n1-n2 if n1>n2 else n2-n1
# print(super_sub(32,56))
#
# def num_check(num):
#     return "even" if num%2==0 else "odd"
# print(num_check(99))

#starts with
# cname="luminar"
# print(cname.startswith("l"))
#
# def is_starts_witha(name):
#     return name.startswith("a")
# print(is_starts_witha("abin"))

# def is_ends_with(name):
#     return name.endswith("k")
# print(is_ends_with("asjklk"))
#
# def is_ends_with(name):
#     return name.endswith("@gmail.com")
# print(is_ends_with("abvcdd@gmail.com"))
# def factorial(num):
#     fact=1
#     for i in range(1,num+1):
#         fact=fact*i
#     return fact
# print(factorial(5))


# def is_prime(num):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#         else:
#          return True
# print(is_prime(45))
# def is_prime(num):
#     for i in range(2,num):
#         return False if num%i==0 else True
# print(is_prime(45))
#
# smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
# print(smart_sub(30,50))
# max=lambda n1,n2:n1 if n1>n2 else n2
# print(max(45,67))
# add=lambda n1,n2:n1+n2
# print(add(32,45))

def is_prime(num):
    flag=0
    for i in range(2,num):
        if num%i==0:
            flag=1
            break

    return  flag==0 
print(is_prime(5))
def prime_range(low,up):
    for num in range(low,(up+1)):
        if is_prime(num):
           print(num)
prime_range(12,21)
























