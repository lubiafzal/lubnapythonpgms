lst=[2,3,4,6]
# sum=8
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         cur_sum=lst[i]+lst[j]
#         if cur_sum==sum:
#             print(lst[i],lst[j])
#             break
#
# lst=[1,2,3,4,5,6]
# sum=8
# for i in range(0,len(lst)):
#     for j in range((i+1),len(lst)):
#         current_sum=lst[i]+lst[j]
#         if current_sum==sum:
#             print(f"pairs{lst[i],lst[j]}")
#             break


lst=[2,3,5,1,4,6]
lst.sort()
element=7
low=0
upp=len(lst)-1
while(low<upp):
    current_sum=lst[low]+lst[upp]
    if current_sum==element:
        print(f"pairs{lst[low],lst[upp]}")
        low+=1
    elif current_sum>element:
        upp-=1
    elif current_sum<element:
        low+=1

lst=[2,3,4,5,6]
sum=8
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        current_sum=lst[i]+lst[j]
        if current_sum==sum:
            print(f'pairs{lst[i]},{lst[j]}')


lst=[2,3,4,5,2,5,1,5,6]
lst.sort()
print(lst)
sum=8
low=0
upp=len(lst)-1
while(low<upp):
    current_sum=lst[low]+lst[upp]
    if current_sum==sum:
        print(f"pairs are {lst[low]},{lst[upp]}")
        low+=1
    elif current_sum>sum:
        upp-=1
    elif current_sum<sum:
        low+=1








