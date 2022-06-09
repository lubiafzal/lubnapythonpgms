

#
# lst1=[1,3,3,4,5,6,5,4,3,4,5]
# dup_lst=[]
# for i in range(0,len(lst1)):
#         for j in range((i+1),len(lst1)):
#                 if lst1[i]==lst1[j]:
#                         dup_lst.append(lst1[j])
# print(dup_lst)
# print(f"first recursive num is {dup_lst[0]},most recursive number{dup_lst[]}")

lst=[1,2,3,4,2,5,5,5]
lst_fre=[]
for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):

         if lst[i]==lst[j]:
               lst_fre.append(lst[i])

print(lst_fre)
print(f"first recursive{lst_fre[0]},most recursive element{lst_fre[1]}")