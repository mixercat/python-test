Friends = ["Mix","Lann","Prame"]
print(Friends)
Friends.append("Mae")
print(Friends)
Friends.remove("Mix")
print(Friends)
del Friends[2]
for i in Friends :
    print(i,end=",")