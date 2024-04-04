class User:

    def __init__(self, first, last, age):
        self.first = first
        self.las = last
        self.yrs = age

    def full_name(self):
            return f"{self.first}  {self.las}"

    def initials(self):
        return f"{self.first[0]}.{self.las[0]}"

    def birthday(self):
        return f"happy birthday {self.first}"

    def likes(self):
        return f"{self.las} likes  "
user1 = User(" john", "engineer", 34)
user2 = User("ian", "mzee", 23)

print(user1.first, user1.las, user1.yrs)
print(user2.first, user2.las, user2.yrs)
print("full name is: ", user2.full_name())
print("    ", user2.initials())
print("    ", user1.initials())
print(user1.birthday())
print(user2.likes())
#
# Class: User
# Objects (Instances): user1 and user2
# Attributes: first, last, and yrs
# Methods: full_name(), initials(), and birthday()
