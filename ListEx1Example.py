menulist = []
pricelist = []

def showbill() :
    print("---- My Food ----")
    for number in range(len(menulist)) :
        print(menulist[number],":",pricelist[number])
    print("-----------------")
    return total(price)

def total(price) :
    print("VAT 7%")
    print(price + (price * 7/100))


while True :
    menuname = input("Enter menu name :")

    if menuname.lower() == "stop" :
        break
    else :
        price = int(input("Enter price :"))
        menulist.append(menuname)
        pricelist.append(price)

showbill()
