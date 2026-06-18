userInput = int(input("Enter Number of Your Favorites Fruits :"))
myFruits = set()
while(len(myFruits)<userInput):
    myFruits.add(input("Fruits : "))
    print(myFruits)