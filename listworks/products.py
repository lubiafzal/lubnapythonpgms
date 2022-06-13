mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 10000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]
]

# no of mobiles
print(f"no of mobiles = {len(mobiles)}")
# total no of available mobiles
available=[mob for mob in mobiles if mob[-1]!=0]
print(f"available mobiles={len(available)}")

# total no of out of stock mobiles
out_stock=[mob for mob in mobiles if mob[-1]==0]
print(f"total no of out of stock mobiles{len(out_stock)}")
# total stock
stock=[mob[-1] for mob in mobiles]
print(f"total no of  mobiles={sum(stock)}")
# print mob in 20 to 30k
twenty_thirty=print([mob for mob in mobiles if mob[-3]>=20000 and mob[-3]<=30000])
twenty_thirty=print([mob  for mob in mobiles if mob[-3] in range(20000,30001)])
# print all 5g mobiles
five_g=print([mob for mob in mobiles if mob[2]=="5g"])
# print all samsung mobiles
samsung=print([mob for mob in mobiles if mob[-2]=="samsung"])
# print costly mobile
max_price=(max([mob[4] for mob in mobiles]))
costly=[mob for mob in mobiles if max_price == mob[4]]
print(costly)
# print low cost mob
low_cost=min([mob[4] for mob in mobiles])
minimum=[mob for mob in mobiles if low_cost==mob[4]]
print(minimum)
# print all mobiles haing stock grt 10
stock_grt_ten=print([mob for mob in mobiles if mob[-1]>10])
# sort mobiles based on price
mobiles.sort(reverse=True,key=lambda mob:mob[-3])
print(mobiles)
# sort according to availability
mobiles.sort(reverse=True,key=lambda mob:mob[-1])
print(mobiles)
# is there any mobile for 10000
vc=[True for mob in mobiles if mob[-3]==60000]
print(vc)

mx_mob=max(mobiles,key=lambda mob:mob[-3])
print(mx_mob)

mn_lowest=min(mobiles,key=lambda mob:mob[-3])
print(mn_lowest)