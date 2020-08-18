class Animal:
    def __init__(self, name, hunger=0):
        self._name = name
        self._hunger = hunger
    def get_name(self):
        return self._name
    def is_hungry(self):
        return self._hunger > 0
    def feed(self):
        self._hunger = self._hunger - 1
    def talk(self):
        pass

class Dog(Animal):
    def __init__(self,name , hunger=0):
        Animal.__init__(self, name , hunger)
    def talk(self):
        Animal.talk(self);
        print("woof woof")
    def specialMethod(self):
        print("There you go, sir!")

class Cat(Animal):
    def __init__(self,name , hunger=0):
        Animal.__init__(self, name , hunger)
    def talk(self):
        Animal.talk(self);
        print("meow")
    def specialMethod(self):
        print("Meeeeow")

class Skunk(Animal):
    def __init__(self,name , hunger=0 , stink_count=6):
        Animal.__init__(self, name , hunger)
        _stink_count = stink_count
    def talk(self):
        Animal.talk(self);
        print("tsssss")
    def specialMethod(self):
        print("Dear lord!")

class Unicorn(Animal):
    def __init__(self,name , hunger=0):
        Animal.__init__(self, name , hunger)
    def talk(self):
        Animal.talk(self);
        print("Good day, darling")
    def specialMethod(self):
        print("I’m not your toy...")

class Dragon(Animal):
    def __init__(self,name , hunger=0 , color="Green"):
        Animal.__init__(self, name , hunger)
        _color = color
    def talk(self):
        Animal.talk(self);
        print("Raaaawr")
    def specialMethod(self):
        print("$@#$#@$")

def main():
    Brownie = Dog("Brownie", 10)
    Zelda = Cat("Zelda" , 3)
    Stinky = Skunk("Stinky" , 0)
    Keith = Unicorn("Keith", 7)
    Lizzy = Dragon("Lizzy" , 1450)
    zoo_lst = [Brownie , Zelda , Stinky , Keith , Lizzy]
    for animal in zoo_lst:
        while animal.is_hungry():
            print(type(animal).__name__ + " " + animal.get_name())
            animal.feed()
            animal.talk()
            animal.specialMethod()

if __name__ == "__main__":
    main()
