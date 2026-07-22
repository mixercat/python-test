class Animal():
    def eat(self):
        print("Rawr! I am eating food.")

class Cat(Animal):
    __name = ""
    def setname(self, text):
        self.name = text
        print("Setting new cat name = " ,self.name)
    def eat(self):
        print("Meow! I am eating cat food.",self.name)

cat1 = Cat()
cat1.setname("Whiskers")
print(cat1._Cat__name)
cat1.eat()