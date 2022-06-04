num1=60
num2=15
num3=90
hcf=1
limit=0
if num1<num2 and num1<num3:
    limit=num1
elif num2<num1 and num2<num3:
    limit=num2
else:
    limit=num3

for i in range(2,(limit+1)):
    if num1%i==0 and num2%i==0 and num3%i==0:
         hcf=i
print(hcf)



