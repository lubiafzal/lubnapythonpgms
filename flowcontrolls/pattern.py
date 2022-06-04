#1234
#1234
#1234

# pat=1234
# for i in range(1,4):
#     print(pat)

# for row in range(1,5):
#     for col in range(1,5):
#         print(col,end="\t")
#     print()
#
# for row in range(1,5):
#     for col in range(1,5):
#         print(row,end="\t")
#     print()
#
# # num=1
# # for row in range(1,5):
#     for col in range(1,row+1):
# #         print(num,end="\t")
# #         num=num+1
# #     print()

# for row in range(1,5):
#     for col in range(1,row+1):
#         print(row,end="\t")
#     print()

# for row in range(1,5):
#     for col in range(1,row+1):
#         print("*",end="\t")
#     print()
#
# for row in range(1,5):
#     for col in range(5,row,-1):
#         print("*",end="\t")
#     print()
# num=5
# k=num-1
# for row in range(1,num):
#     for col in range(1, k):
#         print(end=" ")
#     k=k-1
#     for col in range(1,row+1):
#         print("*",end="\t")
#     print()



# for  row in range(1,5):
#     for space in range(1,5-row):
#         print(" ",end="\t")
#         for col in range(1,row+1):
#             print("*",end="\t")
#     print()

for row in range(1,7):
    str=""
    for space in range(1,7-row):
        str+=" "
    for col in range(1,row+1):
        str+="* "
    print(str)

for row in range(1,7):
    for space in range(1,7-row):
        print(" ",end="")
    for col in range(1,row+1):
        print("*",end=" ")
    print()


for row in range(1,6):
    for col in range(1,10):
        if row==5 or row+col==6 or col-row==4:
             print("*",end=" ")
        else:
            print(" ",end=" ")
    print()