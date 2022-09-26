class Animals:
    def __init__(self, vertebrate, animal_class, name, blood):
        self.__vertebrate = 'vertebrate'
        self.__animal_class = animal_class
        self.name = name
        self.blood = blood


    def eat(self):
        return 'I eat'

    def breath(self):
        return 'I breath'

    def is_vertebrate(self):
        return f'I am {self.__vertebrate}'

    def get_animal_class(self):
        return f'I am from {self.__animal_class}'


class Amphibian(Animals):
    def __init__(self, vertebrate, animal_class, name, blood, skin):
        super().__init__(vertebrate, animal_class, name, blood)
        self.skin = skin

    def breathing(self):
        return "I can Breath with Gills and Lungs"

    def enviroment(self):
        return 'I Spend Part time of their Lives in Water and Part on Land'

    def lay_eggs(self):
        return 'I Lay eggs'

class Bird(Animals):
    def __init__(self, vertebrate, animal_class, name, blood, feather, beak, wings):
        super().__init__(vertebrate, animal_class, name, blood)
        self.feather = feather
        self.beak = beak
        self.wings = wings

    def lay_eggs(self):
        return 'I lay eggs'

    def fly(self):
        return 'Some of us can fly'

class Fish(Animals):
    def __init__(self, vertebrate, animal_class, name, blood, scale, fins):
        super().__init__(vertebrate, animal_class, name, blood)
        self.scale = scale
        self.fins = fins

    def breathing(self):
        return 'I Have gills to breath'

class Mammal:
    def __init__(self, vertebrate, animal_class, name, blood, fur):
        super().__init__(vertebrate, animal_class, name, blood)
        self.fur = fur

    def drink_milk(self):
        return 'Drink milk when I am a baby'

class Reptile(Animals):
    def __init__(self, vertebrate, animal_class, name, blood, scale):
        super().__init__(vertebrate, animal_class, name, blood)
        self.scale = scale

    def breathing(self):
        return 'I beath with lungs'

    def lay_eggs(self):
        return 'I ussually Lay Eggs on Land'

#****************************************************

frog1 = Amphibian('Vertbrate', 'Amphibian', 'Glass frog', 'Cold blood', 'Moist skin')
