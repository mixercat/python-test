price = int(input())

def vatcal(totalPrice) :
    result = totalPrice + (totalPrice * 7/100)
    return result

print(vatcal(price))