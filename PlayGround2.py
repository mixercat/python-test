rent = int(input())
water = int(input())
elec = int(input())
net = int(input())
phone = int(input())

price = 2000
total = price - (rent + water + elec + net + phone)

if total >= 10:
    All = 10
    name = "chewy noodles"
elif total >= 6:
    All = 6
    name = "instant noodles"
elif total >= 2:
    All = 2
    name = "soup"
else: 
    All = 0
    name = "drinking water"

print("RENT  :", rent, "฿")
print("WATER :", water, "฿")
print("ELEC  :", elec, "฿")
print("NET   :", net, "฿")
print("PHONE :", phone, "฿")
print("TOTAL :", rent, "+", water, "+", elec, "+", net, "+", phone)
print("        =", rent + water + elec + net + phone, "฿")
print("SELECT:", name)
print("        =", All, "฿")
print("SAVING:", price, "-", (rent + water + elec + net + phone), "-", All)
print("        =", total - All, "฿")
