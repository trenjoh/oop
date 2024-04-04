class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age =  age
        else:
            self._age = 0

    # def get_age(self):
    #     return self.age
    #
    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self.age = new_age
    #     else:
    #         self.age = 0

    @property # getter
    def age(self):
        return self._age


    @age.setter  #decorators
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative")

    @property
    def full_name(self):
        return f"{self.first} {self.last}"




jane = Human("jane", "goodall", 45)
# print(jane.get_age())
# jane.set_age(34)
# print(jane.get_age())
print(jane.age)
jane.age = 3
print(jane.age)
print(jane.full_name)
