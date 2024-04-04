class Animal:
    cool = True # cool_class attribute

    def make_sound(self, sound):
        print(f"This animal says {sound}")


class Cat(Animal):
    pass

# d = Cat()
Cat().make_sound("MEOW")
# print(d)
# print(Animal.cool)
# print(Cat.cool)
print(isinstance(Animal, Cat))
