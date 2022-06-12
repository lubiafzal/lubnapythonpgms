lst=[
    [10,11],
    [13,45],
    [50,90],
    [60,16],
    [60,70]
]
for sub_list in lst:
    for num in sub_list:
        if num>16:
            print(num)
print(lst)
flt=[]
for arr in lst:
    for num in arr:
        flt.append(num)
print(flt)
print(max(flt))
print(min(flt))
flt_list=[num for sub_list in lst for num in sub_list]
print(sorted(flt_list))
print(sorted(flt_list,reverse=True))
print(max(flt_list))
num_gt_six=[num for num in flt_list if num>16]
print(num_gt_six)
num_odd=print([num for num in flt_list if num%2!=0])
sum_even=print(sum([num for num in flt_list if num%2==0]))

print(flt_list)
mapping=print([num+1 if num>25 else num-1 for num in flt_list])
num_gt_six=print([num for num in flt_list if num>16])

flt_list=[num for sub_list in lst for num in sub_list ]
print(sum(flt_list))