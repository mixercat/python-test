class Customer:
    name = ""
    lastname = ""
    age = 0

    def addCart(self):
        print("Added product to", self.name, self.lastname, "cart.")

customer1 = Customer()
customer1.name = "John"
customer1.lastname = "Doe"
customer1.age = 30
customer1.addCart()

customer2 = Customer()
customer2.name = "Jane"
customer2.lastname = "Smith"
customer2.addCart()

customer3 = Customer()
customer3.name = "Alice"
customer3.lastname = "Johnson"
customer3.addCart()

customer4 = Customer()
customer4.name = "Bob"
customer4.lastname = "Brown"
customer4.addCart()