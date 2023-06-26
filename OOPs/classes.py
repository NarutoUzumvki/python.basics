mylist = [1,2,3]
mylist.append(4)
print(mylist)



#  CLASS

class Demo():
    pass
x= Demo()
print(type(x))

#  ** CLASS EXAMPLES **

class Dog():
    pass
mydog=Dog()
print(type(mydog))


#  CREATING ATTRIBUTES 

class Dog():
    def __init__(self):
        pass
mydog=Dog()
print(type(mydog))

#  ADDING MORE ATTRIBUTES

class Dog():
    def __init__(self,breed):
        self.breed=breed
mydog = Dog(breed='Huskie')
print("My dog's Breed is :" + " " + mydog.breed)
other_dog = Dog("Lab")
print("Other dog's Breed is :" + " " + other_dog.breed)

# MORE EXAMPLES

class Dog():

    # CLASS OBJECT ATTRIBUTE

    species= "Mammal"

    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
dog1=Dog("Lab","Brownie")
dog2=Dog("","bear")

print(dog1.breed)
print(dog2.name)
print(dog2.species)