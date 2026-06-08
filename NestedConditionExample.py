Username = input("Enter your Username: ")
Password = input("Enter your Password: ")

x = "admin"
y = "1234"

if Username == x and Password == y :
    print("Welcome Admin")
    current_user_role = "Admin"
elif Username == Username and Password == Password :
    print("Welcome guest")
    current_user_role = "Guest"
else :
    print("error")

if current_user_role == "Admin" :
    print("You have full access to the system")
elif current_user_role == "Guest" :
    print("You have limited access to the system")