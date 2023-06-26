class Animal:
    
    def __init__(self):
        print("Animal Created!")

    def Who_Am_I(self):
        print("ANIMAL")

    def Eat(self):
        print("Eating!")


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("CAT CREATED!")
    
    def sound(self):
        print("Meow..!")


ani=Animal()
ani.Who_Am_I() 
ani.Eat()

ct=Cat()
ct.Who_Am_I()
ct.Eat()
ct.sound()