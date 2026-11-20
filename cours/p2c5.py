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