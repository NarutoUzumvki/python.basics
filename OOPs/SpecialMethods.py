print("")
class Book:
    def __init__(self,title,author,page):
        self.title=title
        self.author=author
        self.page=page

print(" before using the Special method __str__   ")

# Some Jumbled Code Along with __main__.Book 
# Will result as Output While printing(b).

b=Book("Time","Matter",11)
print(b)

print("")



# Here after using the special method __str__ the result gets printed in String Format.

class Book:
    def __init__(self,title,author,page):
        self.title=title
        self.author=author
        self.page=page

    def __str__(self):
        return " Title : {} , Author : {} , Page : {} ".format(self.title,self.author,self.page)

print(" After using the Special method __str__   ")

bo=Book("Will","Anonymous",123)
print(bo)

print("")



# Now We use anothe special method in this class known as __len__ where the len() built-in func. checks for whether if the class contains any __len__ function and if thats true it returns whatever the method tells it to return.


class Book:
    def __init__(self,title,author,page):
        self.title=title
        self.author=author
        self.page=page

    def __str__(self):
        return " Title : {} , Author : {} , Page : {} ".format(self.title,self.author,self.page)

    def __len__(self):
        return self.page

bo=Book("Will","Anonymous",123)
print(bo)


print(" After using the Special method __len__   ")

print(len(bo))









# b.title()
# b.author()
# b.page
