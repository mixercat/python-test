def login():
    Name = input("Enter your name :")
    password = input("Enter your password :")

    if Name == "Admin" and password == "1234" :
        Current_User = "Admin"
        print("Welcome Admin")

    elif Name == "mix" and password == "1234" :
        Current_User = "Guest"
        print("welcome Guest to shop")
        print("------------------------------")
        print("Do you want to buy anything?")
        return showMenu()


def showMenu():
    print("-------------------------------------------")
    print("Banana     : 10      Baht")
    print("Apple      : 20      Baht")
    print("Orange     : 15      Baht")
    print("Computer   : 15000   Baht")
    print("Gpu        : 30000   Baht")
    print("Cpu        : 20000   Baht")
    print("Cooler     : 5000    Baht")
    print("Ram        : 8000    Baht")
    print("Ssd        : 4000    Baht")
    print("Hdd        : 3000    Baht")
    print("-------------------------------------------")
    return menuSelect()
    

def menuSelect():
    Banana = 10
    Apple = 20
    Orange = 15
    Computer = 15000
    Gpu = 30000
    Cpu = 20000
    Cooler = 5000
    Ram = "Out Stock"
    Ssd = "Out Stock"
    Hdd = "Out Stock"

    current_price = 0

    while True:
        user_choice = input("Which product are you interested in buying? : ")
    
        if user_choice == "Stop":
            break     
        elif user_choice == "Banana":
            print("Price of Banana is :", Banana, "Baht")
            current_price += Banana       
        elif user_choice == "Apple":
            print("Price of Apple is :", Apple, "Baht")
            current_price += Apple        
        elif user_choice == "Orange":
            print("Price of Orange is :", Orange, "Baht")
            current_price += Orange        
        elif user_choice == "Computer":
            print("Price of Computer is :", Computer, "Baht")
            current_price += Computer        
        elif user_choice == "Gpu":
            print("Price of Gpu is :", Gpu, "Baht")
            current_price += Gpu        
        elif user_choice == "Cpu":
            print("Price of Cpu is :", Cpu, "Baht")
            current_price += Cpu       
        elif user_choice == "Cooler":
            print("Price of Cooler is :", Cooler, "Baht")
            current_price += Cooler        
        elif user_choice == "Ram":
            print("Ram is :", Ram)        
        elif user_choice == "Ssd":
            print("Ssd is :", Ssd)       
        elif user_choice == "Hdd":
            print("Hdd is :", Hdd)       
        else:
            print("Sorry, we don't have this product.")

    return PrcieCalculator(current_price) 

        
def PrcieCalculator(price):
    Total = price + (price * 7/100)
    print("Vat 7% :",price * 7/100)
    print("-------------------------------------------")
    print("Total price (included VAT 7%):", Total, "Baht")

login()