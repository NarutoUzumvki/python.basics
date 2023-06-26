#  ** Classes With Both Methods And Attributes **

class Circle():

    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius

myc=Circle()
print(myc.radius)


# MORE EXAMP.
# SO NOW LET'S CREATE A METHOD 
# REMEMBER METHODS ARE BUILT INSIDE THE BODY OF A CLASS..


class Circle:
    pi=3.14

    def __init__(self,radius=4):
        self.radius=radius

    def area(self):
        return Circle.pi*(self.radius**2)
        
    def area(self):
        return Circle.pi*(self.radius**2)

my=Circle(3)
print(my.radius)
print(my.area())

# ADDING ONE MORE METHOD IN THE CLASS

class Circle():
    pi=3.14

    def __init__(self,radius=2):
        self.radius=radius

    def area(self):
        return Circle.pi * (self.radius**2)

    def set_radius(self,new_r):
        self.radius=new_r

myc=Circle(4)
print(myc.radius)

myc.set_radius(555)
print(myc.radius)
print(myc.area())
    


