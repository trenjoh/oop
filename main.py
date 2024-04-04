# object-oriented programming
# method of programming that attempts to model some process as class/object
# class-a blueprint of object.Can contain functions ...
# objects-instances of class
# instance- objets that are constructed from a class blueprint that contain their
# ...class's methods and properties

# introduction to  class

class User:

    def __init__(self, first, last, age):
        self.first = first
        self.las = last
        self.yrs = age
user1 = User(input("Enter your name  "), "engineer", 34)
user2 = User("ian", "mzee", 23)

print("name :", user1.first, user1.las, "\n age:", user1.yrs, "ageing")
print(user2.first, user2.las, user2.yrs)

# significance of underscores
# _name: sth to be internally used
# __name
# __name__ : python specific methods
