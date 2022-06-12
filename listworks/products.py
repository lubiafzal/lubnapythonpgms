mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]
]
print(f"total no of mobiles= {len(mobiles)}")
# available no of mobiles
available=[mob for mob in mobiles if mob[-1]!=0]
print(f"total no of available mobiles={len(available)}")
# total no of out of stock mobiles
out_stock=(([mob for mob in mobiles if mob[-1]==0 ]))
print(f"number of out of stock mobiles={len(out_stock)}")
# total stock
total_stock=[mob[-1] for mob in mobiles if mob[-1]!=0]
print(f"total stock of mobiles = {sum(total_stock)}")
# print mobiles btwn 20 to 30
twenty_to_thirty=print([mob for mob in mobiles if mob[4]>20000 and mob[4]<30000])
# print all 5g mobiles
five_g_mob=print([mob for mob in mobiles if mob[2]=="5g"])
# print all samsung phones
samsung_mobiles=print([mob for mob in mobiles if mob[-2]=="samsung"])
# print costly mob
costly_mob=sorted([mob for mob in mobiles ])
print(costly_mob[-1])
# print all mobiles having stock gt 10
stock_gt_10=([mob for mob in mobiles if mob[-1]>10])
print(stock_gt_10)
# count of mobiles having display amoled
display_amoled=([mob for mob in mobiles if mob[3]=="AMOLED"])
print(f"number of mobiles with display amoled {len(display_amoled)}")
# sort the mobiles based on price in descending order
price_mob=([mob for mob in mobiles ])
print(sorted(price_mob[-3],reverse=True))

# sort the mobile based on availability


