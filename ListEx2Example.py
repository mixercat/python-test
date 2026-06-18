systemMenu = {"Rice" : 45,"Chicken" : 50,"Beef steak" : 120,"Pork steak" : 100,"Water" : 15}
menulist = []

def showbill() :
    print("---- My Food ----")
    total_price = 0

    for number in range(len(menulist)) :
        print(menulist[number][0], menulist[number][1])
        total_price += menulist[number][1]
    total(total_price)

def total(price) :
    print("VAT 7%")
    print(price + (price * 7/100))

while True :
    menuname = input("Enter menu name :")

    if menuname.lower() == "stop" :
        break
    else :
        menulist.append([menuname,systemMenu[menuname]])

showbill()