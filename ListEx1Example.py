menulist = []

def showbill() :
    print("---- My Food ----")
    for number in range(len(menulist)) :
        print(menulist[number][0], menulist[number][1])
    return total(menuprice)

def total(price) :
    print("VAT 7%")
    print(price + (price * 7/100))


while True :
    menuname = input("Enter menu name :")

    if menuname.lower() == "stop" :
        break
    else :
        menuprice = int(input("Enter price :"))
        menulist.append([menuname,menuprice])

showbill()
