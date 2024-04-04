class User:
    active_user =0

    @classmethod
    def display_active_user(cls):
        return f"there are currently {cls.active_user} active users"

    def __init__(self, first, last, age):
        self.first = first
        self.las = last
        self.yrs = age
        User.active_user += 1

    def logout(self):
        User.active_user -= 1
        return f"{self.first} has logged out"

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

print(User.display_active_user())
# user1 = User(" john", "engineer", 34)
# user2 = User("ian", "mzee", 23)
# print(User.display_active_user())
# user1 = User(" john", "engineer", 34)
# user2 = User("ian", "mzee", 23)
# print(user1.logout())
print(user2.logout())
print(user1.logout())
print(f"There are currently {User.display_active_user()} active users")
print(user1.full_name())

