"""while True :
    Number = int(input())
    print("Number :",Number)

    if Number > 0 :
        Cal = Number * "*"
        print(Cal)
    elif Number == 0 :
        print("None")
    else :
        print("error")
    break"""

Number = int(input())
print(Number)

for i in range(1,Number+1) :
    print(i * "*")