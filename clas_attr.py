# class attributes
class Pet:

    allowed = ['cat', 'dog', 'fish', 'cow']

    def __init__(self, name, species) -> None:
        if species not in Pet.allowed:
            raise ValueError(f"you can't have a {species} pet !")
        self.name = name
        self.species = species
    def set_species(self,species):
        if species not in Pet.allowed:
            raise ValueError(f"{species}not found ")
        self.species= species

cat = Pet("Blue", "cat")
dog = Pet("yellow", "dog")

print(cat.name)
print(f"Cat's species: {cat.species}")
print(Pet.allowed)

print(id(Pet.allowed))