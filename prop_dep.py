class Animal:

    def __init__(self, name, species):
        self.name = name
        self.species = species


    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):  # inheritance
    def __init__(self, name, species, breed, toy):
        # Animal.__init__(self, name, species)
        super().__init__(name, species)
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name}  plays with {self.toy}")

    def __repr__(self):
        return f"{self.name} is a {self.species}"

blue = Cat("Blue", "Cat", "Scottish fold", "strings")
print(blue)
print(blue.species)
print(blue.toy)
print(blue.breed)
blue.play()

