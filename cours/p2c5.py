from classes.toolbox import Screwdriver, Hammer, Nail

class Person:
    """Personne."""

    def __init__(self, name):
        """Donne un nom."""
        self.name = name
    
    def walk(self):
        """Marche."""
        print(f"{self.name} marche.")


volunteers = [Person("Alice"), Person("Bob"), Person("Carol")]
for volunteer in volunteers:
    volunteer.walk()

# Ici, nous reprenons nos outils !
toolbox = {
    "screwdriver": Screwdriver(50),
    "hammer": Hammer(),
    "nails": [Nail(), Nail(), Nail()],
}

class Human:
    def run(self):
        print("Je cours !")

class Lion:
    def run(self):
        print("Roar !!")

class Fish:
    def swim(self):
        print("Bloup bloup")

entities = [Human(), Lion()]
# entities = [Human(), Lion(), Fish()] => AttributeError: 'Fish' object has no attribute 'run'
for entity in entities:
    entity.run()

from typing import List

def highest(numbers: List[int]) -> int:
    max_value = 0
    for number in numbers:
        if number > max_value:
            max_value = number
    return max_value

def divide(a, b):
    assert b != 0 # (affirmer) – souvent utilisée dans les tests – cause le déclenchement d’une Exception par un programme si quelque chose n’est pas vrai - déconseillé pour un code de production
    return a / b

for volunteer in volunteers:
    if hasattr(volunteer, "walk"):
        volunteer.walk()

"""if not isinstance(x, Y):
    raise Z("M")"""