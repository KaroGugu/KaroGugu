class Zoo:
    __animals = 0  # a class attribute that stores the total count of the animals in the zoo

    def __init__(self, name):  # only receive the name of the zoo
        self.name = name
        self.mammals = []    # create 3 empty lists (mammals, fishes, birds)
        self.fishes = []
        self.birds = []

    def get_animals_count(self):   # we define additional method to get the private __animals = 0
        return self.__animals

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

        self.__animals += 1        # Zoo.__animals += 1   if we don't hare the get_animal_count

    def get_info(self, species):
        if species == "mammal":
            return f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            return f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            return f"Birds in {self.name}: {', '.join(self.birds)}"


name = input()
n = int(input())
zoo = Zoo(name)

for _ in range(n):
    species, name = input().split()
    zoo.add_animal(species, name)

searched_species = input()
print(zoo.get_info(searched_species))
print(f"Total animals: {zoo.get_animals_count()}")